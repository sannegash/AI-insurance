from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render
from rest_framework.exceptions import ValidationError
from rest_framework import status
import requests
import uuid

def home(request):
    return render(request,'chapa.html')
def transfer(requets):
    return render(request,'transfer.html')