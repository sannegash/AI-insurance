from rest_framework import serializers
from .models import Claim

class ClaimSerializer(serializers.ModelSerializer):
   class Meta: 
        model = Claim
        fields = ['vehicle', 'claimant', 'claim_date', 'accident_date', 'accident_location',
        'description', 'estimated_damage_cost', 'police_report_number', 'status', 'claim_officer', 
        'created_at', 'updated_at',
        ]