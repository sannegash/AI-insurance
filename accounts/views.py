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



class SubmitCustomerDataAPIView(APIView):
    def post(self, request):
        serializer = CombinedCustomerDataSerializer(data=request.data)

        if serializer.is_valid():
            chassis_number = serializer.validated_data.get("chassis_number")
            username = serializer.validated_data.get("username")
            
            # Check if a vehicle with the given chassis number already exists
            if Vehicle.objects.filter(chassis_number=chassis_number).exists():
                return Response(
                    {"message": "This vehicle has already been submitted!"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            try:
                # Get the NewCustomer instance
                new_customer = NewCustomer.objects.get(id=customer_id)

                # Create the vehicle and driver instances and link to the customer
                vehicle = Vehicle.objects.create(
                    chassis_number=chassis_number,
                    owner_name=serializer.validated_data["owner_name"],
                    vehicle_make=serializer.validated_data["vehicle_make"],
                    vehicle_year=serializer.validated_data["vehicle_year"],
                    fuel_type=serializer.validated_data["fuel_type"],
                    transmission_type=serializer.validated_data["transmission_type"],
                    engine_capacity=serializer.validated_data["engine_capacity"],
                    color=serializer.validated_data["color"],
                    customer=new_customer,  # Link to NewCustomer
                )

                driver = Driver.objects.create(
                    name=serializer.validated_data["driver_name"],
                    license_number=serializer.validated_data["driver_license_number"],
                    vehicle=vehicle  # Link to Vehicle
                )

                return Response({"message": "Customer data successfully submitted!"}, status=status.HTTP_201_CREATED)
            except Exception as e:
                # Log or print the exception for debugging
                print(f"Error saving data: {e}")
                return Response({"message": "An error occurred while saving data."}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

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
