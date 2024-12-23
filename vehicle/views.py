from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Vehicle, Driver 
from .serializers import VehicleSerializer, DriverSerializer

class VehicleViewSet(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

class DriverViewSet(viewsets.ModelViewSet):
    queryset = Driver.objects.all()
    serializer_class = DriverSerializer

