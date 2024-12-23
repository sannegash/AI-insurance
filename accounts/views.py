from rest_framework import viewsets
from django.shortcuts import render
from rest_framework import generics
from .models import NewCustomer, Underwriter, Cashier, ClaimOfficer
from .serializers import  NewCustomerSerializer, UnderwriterSerializer, CashierSerializer, ClaimOfficerSerializer


class NewCustomerViewSet(viewsets.ModelViewSet):
    queryset = NewCustomer.objects.all()
    serializer_class = NewCustomerSerializer

class UnderwriterViewSet(viewsets.ModelViewSet):
    queryset = Underwriter.objects.all()
    serializer_class = UnderwriterSerializer

class CashierViewSet(viewsets.ModelViewSet):
    queryset = Cashier.objects.all()
    serializer_class = CashierSerializer

class ClaimOfficerViewSet(viewsets.ModelViewSet):
    queryset = ClaimOfficer.objects.all()
    serializer_class = ClaimOfficerSerializer
