from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import RiskAssessment 
from .serializers import RiskAssessmentSerializer
from accounts.models import NewCustomer 
import random
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets
from .serializers import RiskAssessmentSerializer
from vehicle.models import Vehicle

class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer

    @action(detail=True, methods=['post'])
    def ai_prediction(self, request, pk=None):
        """
        Randomly assigns a risk factor and claim likelihood to a vehicle.
        """
        try:
            # Fetch the vehicle by its primary key (pk)
            vehicle = Vehicle.objects.get(id=pk)
        except Vehicle.DoesNotExist:
            return Response({"error": "Vehicle not found."}, status=404)

        # Randomly assign risk factor from available choices
        risk_factors = ['High', 'Medium', 'Low']
        risk_factor = random.choice(risk_factors)

        # Randomly assign claim likelihood between 0 and 100 (percentage)
        claim_likelihood = round(random.uniform(0, 100), 2)  # Random float between 0 and 100, rounded to 2 decimal places
        claim_likelihood = min(max(claim_likelihood, 0), 100)  # Random float between 0 and 100, rounded to 2 decimal places

        # Create or update the RiskAssessment for the vehicle
        risk_assessment, created = RiskAssessment.objects.update_or_create(
            vehicle=vehicle,  # Now referencing the vehicle
            defaults={
                'risk_factor': risk_factor,
                'claim_likelihood': claim_likelihood
            }
        )

        # Serialize and return the risk assessment
        serializer = RiskAssessmentSerializer(risk_assessment)
        return Response(serializer.data)