from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Claim
from .views import ClaimViewSet

router = DefaultRouter()

router.register(r'claim',ClaimViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]