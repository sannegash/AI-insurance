from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import RiskAssessment 
from .serializers import RiskAssessmentSerializer

class RiskAssessmentViewSet(viewsets.ModelViewSet):
    queryset = RiskAssessment.objects.all()
    serializer_class = RiskAssessmentSerializer
