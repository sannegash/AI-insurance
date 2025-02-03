from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle, Driver
from accounts.models import NewCustomer 
from .serializers import VehicleSerializer, DriverSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated] 
    def get_queryset(self):
        # Return only the vehicles associated with the authenticated user
        return Vehicle.objects.filter(customer__user=self.request.user)

    def perform_create(self, serializer):
        # Ensure that the user is associated with the new vehicle when creating
        new_customer = self.request.user.newcustomer
        serializer.save(customer=new_customer)

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer
    authentication_classes = [JWTAuthentication]  # Use JWT for authentication
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Driver.objects.filter(vehicle__customer__user=self.request.user)

    def perform_create(self, serializer):
        user = self.request.user
        try:
            customer = NewCustomer.objects.get(user=user)
            vehicle = Vehicle.objects.get(customer=customer)  # Get the user's vehicle
            serializer.save(vehicle=vehicle)  # Assign the driver to the correct vehicle
        except (NewCustomer.DoesNotExist, Vehicle.DoesNotExist):
            raise serializers.ValidationError("No associated vehicle found for this user.")
