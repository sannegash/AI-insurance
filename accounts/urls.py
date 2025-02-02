from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewCustomerViewSet, UnderwriterViewSet, CashierViewSet, ClaimOfficerViewSet
from . import views

# Initialize the router
router = DefaultRouter()

# Register viewsets with basenames to avoid ambiguity
router.register(r'newcustomers', NewCustomerViewSet, basename='newcustomer')  # Add basename for NewCustomer
router.register(r'underwriters', UnderwriterViewSet, basename='underwriter')  # Add basename for Underwriter
router.register(r'cashiers', CashierViewSet, basename='cashier')  # Add basename for Cashier
router.register(r'claimofficers', ClaimOfficerViewSet, basename='claimofficer')  # Add basename for ClaimOfficer

# Define the URL patterns
urlpatterns = [
    path('api/', include(router.urls)),  # Include the router URLs
    path('verify-new-customer/<int:customer_id>/', views.verify_new_customer, name='verify_new_customer'),
]
