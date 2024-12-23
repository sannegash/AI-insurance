from rest_framework import serializers
from .models import RiskAssessment

class RiskAssessmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiskAssessment
        fields = [ 'risk_factor', 'claim_likelihood', 'created_at', 'updated_at']
