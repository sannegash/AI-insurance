from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Policy 
from .views import PolicyViewSet

router = DefaultRouter()

router.register(r'policies',PolicyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]