from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.exceptions import PermissionDenied
from .models import Claim
from .serializers import ClaimSerializer


class ClaimViewSet(viewsets.ModelViewSet):
    """ Viewset for managing claims """
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
    """Allow underwriters to verify the claim and calculate estimated damage cost"""
    try:
        claim = Claim.objects.get(id=claim_id)
    except Claim.DoesNotExist:
        return Response({'error': 'Claim not found'}, status=status.HTTP_404_NOT_FOUND)

    if not request.user.groups.filter(name='Underwriter').exists():
        return Response({'error': 'Permission denied'}, status=status.HTTP_403_FORBIDDEN)

    # Prevent modification if the claim is already approved or rejected
    if claim.status in ['Approved', 'Rejected']:
        return Response({'error': 'This claim has already been processed.'}, status=status.HTTP_400_BAD_REQUEST)

    # Check and update the 'estimated_damage_cost' and 'description'
    estimated_damage_cost = request.data.get('estimated_damage_cost')
    description = request.data.get('description')

    if estimated_damage_cost is None:
        return Response({'error': 'Estimated damage cost is required'}, status=status.HTTP_400_BAD_REQUEST)

    claim.estimated_damage_cost = estimated_damage_cost
    if description:
        claim.description = description
    claim.save()

    return Response({'message': 'Claim verified successfully'}, status=status.HTTP_200_OK)


@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def approve_or_deny_claim(request, claim_id):
    """Allow claim officers to approve or deny the underwriter's claim estimate"""
    try:
        claim = Claim.objects.get(id=claim_id)
    except Claim.DoesNotExist:
        return Response({'error': 'Claim not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user is a claim officer
    if not request.user.groups.filter(name='Claim Officer').exists():
        raise PermissionDenied("You do not have permission to approve or deny claims.")
    
    # Check if the claim is in the 'Pending' status and the estimated damage cost is provided
    if claim.status != 'Pending' or claim.estimated_damage_cost is None:
        return Response({'error': 'This claim has either been already processed or is missing the estimated damage cost.'}, status=status.HTTP_400_BAD_REQUEST)

    # Get the action (approve or deny) from the request data
    action = request.data.get('action')

    if action not in ['approve', 'deny']:
        return Response({'error': 'Action must be either "approve" or "deny".'}, status=status.HTTP_400_BAD_REQUEST)

    if action == 'approve':
        # Set the claim status to 'Approved'
        claim.status = 'Approved'
        claim.save()
        return Response({'message': 'Claim approved successfully.'}, status=status.HTTP_200_OK)

    if action == 'deny':
        # Set the claim status to 'Rejected'
        claim.status = 'Rejected'
        claim.save()
        return Response({'message': 'Claim rejected successfully.'}, status=status.HTTP_200_OK)
