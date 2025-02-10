from rest_framework import serializers
from .models import Claim
from vehicle.models import Vehicle
from rest_framework import serializers
from .models import Claim, Vehicle, User

class ClaimSerializer(serializers.ModelSerializer):
    vehicle = serializers.PrimaryKeyRelatedField(queryset=Vehicle.objects.all())

    class Meta:
        model = Claim
        fields = [
            'id', 'vehicle', 'claim_date', 'estimated_damage_cost', 'accident_date', 'accident_location', 
            'description', 'settlement_amount', 'police_report_number', 'status',  
            'created_at', 'updated_at'
        ]
        read_only_fields = ['claim_date', 'created_at', 'updated_at']  # Fields that should not be modified directly

    def validate_vehicle(self, value):
        if not value:
            raise serializers.ValidationError("Vehicle field cannot be empty.")
        return value

    def validate_status(self, value):
        if value not in dict(Claim.STATUS_CHOICES).keys():
            raise serializers.ValidationError("Invalid status value.")
        return value
