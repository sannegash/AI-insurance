from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import RiskAssessment 
from .views import RiskAssessmentViewSet

router = DefaultRouter()

router.register(r'risk',RiskAssessmentViewSet)


urlpatterns = [
    path('api/', include(router.urls)),
]