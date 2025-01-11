from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Vehicle, Driver 
from .views import VehicleViewSet, DriverViewSet

router = DefaultRouter()

router.register(r'vehicle',VehicleViewSet)
router.register(r'Driver',DriverViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]