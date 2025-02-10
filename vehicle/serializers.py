from rest_framework import serializers
from .models import Vehicle, Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'driver_firstname', 
            'driver_lastname', 
            'licence_number'
        ]

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [
            'id',
            'chassis_number', 
            'registration_number', 
            'owner_name', 
            'vehicle_make', 
            'vehicle_model', 
            'vehicle_year', 
            'fuel_type', 
            'transmission_type', 
            'engine_capacity', 
            'color', 
            'created_at', 
            'updated_at'
        ]
