from rest_framework import serializers
from .models import Vehicle, Driver

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = [
            'vehicle', 
            'driver_firstname', 
            'driver_lastname', 
            'licence_number'
        ]

class VehicleSerializer(serializers.ModelSerializer):
    # Serializing drivers linked to the vehicle
    driver = DriverSerializer( read_only=True)

    class Meta:
        model = Vehicle
        fields = [
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
            'driver',  # Include related drivers in the serialized data
            'created_at', 
            'updated_at'
        ]
