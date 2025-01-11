from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Claim
from .serializers import ClaimSerializer
from rest_framework.permissions import IsAuthenticated

class ClaimViewSet(viewsets.ModelViewSet):
    """ viewset for managign claims."""
    queryset = Claim.objects.all()
    serializer_class = ClaimSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        """
        Limit queryset based on user type:
        - Insured customers can only see their claims.
        - Underwriters see all claims.
        """
        if self.request.user.groups.filter(name='Underwriter').exists():
            return Claim.objects.all()
        return Claim.objects.filter(claimant=self.request.user.newcustomer)

    def perform_create(self, serializer):
        """
        Ensure that 'estimated_damage_cost' is excluded during claim creation.
        Associate the claim with the logged-in customer.
        """
        serializer.save(claimant=self.request.user.newcustomer, estimated_damage_cost=None)

    def get_serializer(self, *args, **kwargs):
        """
        Dynamically adjust the serializer fields:
        - Remove 'estimated_damage_cost' for insured customers.
        """
        serializer_class = self.get_serializer_class()
        kwargs['context'] = self.get_serializer_context()
        serializer = serializer_class(*args, **kwargs)

        # Remove 'estimated_damage_cost' field for insured customers
        if not self.request.user.groups.filter(name='Underwriter').exists():
            serializer.fields.pop('estimated_damage_cost', None)

        return serializer

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def verify_claim(request, claim_id):
    """Allow underwriter to verify the claim and calculate estimated damage cost"""
    try:
        claim = Claim.objects.get(id=claim_id)
    except Claim.DoesNotExist:
        return Response({'error': 'Claim not found'}, status=status.HTTP_404_NOT_FOUND)

    if not request.user.groups.filter(name='Underwriter').exists():  # Check underwriter role
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    # Prevent modification if the claim is already approved or rejected
    if claim.status in ['Approved', 'Rejected']:
        return Response({'error': 'This claim has already been processed.'}, status=status.HTTP_400_BAD_REQUEST)

    # Only allow updating certain fields
    estimated_damage_cost = request.data.get('estimated_damage_cost')
    status = request.data.get('status', 'Approved')  # Default to Approved if not provided

    if estimated_damage_cost is None:
        return Response({'error': 'Estimated damage cost is required'}, status=status.HTTP_400_BAD_REQUEST)

    claim.estimated_damage_cost = estimated_damage_cost
    claim.status = status
    claim.save()

    return Response({'message': 'Claim verified successfully'}, status=status.HTTP_200_OK)
