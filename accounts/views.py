from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.exceptions import PermissionDenied
from django.shortcuts import render
from rest_framework import generics
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer
from .serializers import  NewCustomerSerializer, UnderwriterSerializer, CashierSerializer, ClaimOfficerSerializer, CombinedCustomerDataSerializer
from rest_framework.views import APIView
from  vehicle.models  import Vehicle 
from core.models import User


class NewCustomerViewSet(viewsets.ModelViewSet):
    queryset = NewCustomer.objects.all()
    serializer_class = NewCustomerSerializer
    def get_queryset(self):
        queryset = super().get_queryset()
        username = self.request.query_params.get('username', None)
        if username:
            queryset = queryset.filter(user__username__iexact=username)  # Filter based on username field of the User model
        return queryset 
class UnderwriterViewSet(viewsets.ModelViewSet):
    queryset = Underwriter.objects.all()
    serializer_class = UnderwriterSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])  # Ensure the user is authenticated
def create_new_customer(request):
    user = request.user  # Get the logged-in user

    # Check if a NewCustomer object already exists for this user
    if NewCustomer.objects.filter(user=user).exists():
        return Response({"error": "User already has a NewCustomer profile."}, status=status.HTTP_400_BAD_REQUEST)

    # Attach the user to the request data
    data = request.data.copy()
    data['user'] = user.id  # Set the user ID

    serializer = NewCustomerSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def verify_new_customer(request, customer_id):
    """Allow underwriter to verify and convert new customer to insured customer."""
    
    try:
        customer = NewCustomer.objects.get(id=customer_id)
    except NewCustomer.DoesNotExist:
        return Response({'error': 'Customer not found'}, status=status.HTTP_404_NOT_FOUND)

    # Check if the user is an underwriter
    if not request.user.groups.filter(name='Underwriter').exists():
        raise PermissionDenied("You do not have permission to verify customers.")
    
    # If the customer is already insured or rejected, prevent changing status
    if customer.status in ['Insured', 'Rejected']:
        return Response({'error': 'This customer is already verified or rejected.'}, status=status.HTTP_400_BAD_REQUEST)

    # Update the status of the new customer to "Insured"
    customer.status = 'Insured'
    customer.save()

    return Response({'message': 'Customer successfully verified and converted to Insured.'}, status=status.HTTP_200_OK)
class CashierViewSet(viewsets.ModelViewSet):
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

class ClaimOfficerViewSet(viewsets.ModelViewSet):
    queryset = ClaimOfficer.objects.all()
    serializer_class = ClaimOfficerSerializer
