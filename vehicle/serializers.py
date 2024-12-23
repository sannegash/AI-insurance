from rest_framework import serializers
from .models import Vehicle, Driver

class VehicleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vehicle
        fields = [ 
            'customer', 'registration_number', 'owner_name', 'vehicle_make', 'vehicle_year', 'fuel_type', 'transmission_type', 'engine_capacity', 'color', 'chassis_number', 'created_at','updated_at'
        ]

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'vehicle', 'driver_firstname', 'driver_lastname', 'licence_number'
        ]