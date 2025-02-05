from rest_framework import serializers
from .models import Policy

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = [ 
            'policy_number',  'vehicle', 'policy_type', 'coverage_start_date', 'coverage_end_date', 
            'premium_amount', 'insured_value', 'policy_holder', 'status', 'created_at', 'updated_at'
        ]
        def validate_vehicle(self, value):
            try:
                # Look for the vehicle by chassis number (which is a unique field)
                vehicle = Vehicle.objects.get(chassis_number=value)
            except Vehicle.DoesNotExist:
                raise serializers.ValidationError("No vehicle matches the given chassis number.")
            return vehicle