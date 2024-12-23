from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import Policy
from .serializers import PolicySerializer

class PolicyViewSet(viewsets.ModelViewSet):
    queryset = Policy.objects.all()
    serializer_class = PolicySerializer

