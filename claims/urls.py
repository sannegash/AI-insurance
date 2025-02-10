from django.urls import path
from .models import Claim
from . import views

urlpatterns = [
    path('claims/', views.create_claim, name='create_claim'),  # Create a new claim
    path('claims/list/', views.get_claims, name='get_claims'),  # Get all claims
    path('claims/<int:pk>/', views.update_claim, name='update_claim'),  # Get or update a specific claim
]

