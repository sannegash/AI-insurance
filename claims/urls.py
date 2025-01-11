from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Claim
from .views import ClaimViewSet
from . import views
router = DefaultRouter()

router.register(r'claim',ClaimViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('verify-claim/<int:claim_id>/', views.verify_claim, name='verify_claim'),
]