from rest_framework import serializers
from .models import Policy

class PolicySerializer(serializers.ModelSerializer):
    class Meta:
        model = Policy
        fields = [ 
            'policy_number', 'insured_name', 'vehicle', 'policy_type', 'coverage_start_data', 'coverage_end_date', 
            'premium_amount', 'insured_value', 'policy_holder', 'status', 'created_at', 'update_at'
        ]
