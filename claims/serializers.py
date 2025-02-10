from rest_framework import serializers
from .models import Claim

class ClaimSerializer(serializers.ModelSerializer):
    class Meta:
        model = Claim
        # Include all fields in the model, but control which are required
        fields = ['vehicle', 'claimant', 'claim_date', 'accident_date', 'accident_location',
                  'description', 'estimated_damage_cost', 'police_report_number', 'status', 'claim_officer', 
                  'created_at', 'updated_at']
        
        # Specify which fields are required during claim creation
        extra_kwargs = {
            'accident_date': {'required': True},
            'accident_location': {'required': True},
            'police_report_number': {'required': True},
            'claim_date': {'required': True},
            'vehicle': {'required': True},
            # Mark other fields as not required for creation

            'description': {'required': False},
            'estimated_damage_cost': {'required': False},
            'status': {'required': False},
            'claim_officer': {'required': False},
            'created_at': {'required': False},
            'updated_at': {'required': False},
        }

    def validate(self, data):
        """
        You can add any additional validation if necessary here
        """
        return data
