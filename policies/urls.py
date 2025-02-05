from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .models import Policy 
from .views import PolicyViewSet, CustomerListView, PolicyCreateView

router = DefaultRouter()

router.register(r'policies',PolicyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('customers/', CustomerListView.as_view(), name='customer-list'),
    path("create-policy/", PolicyCreateView.as_view(), name="create-policy"),
]