from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewCustomerViewSet, UnderwriterViewSet, CashierViewSet, ClaimOfficerViewSet, SubmitCustomerDataAPIView
from . import views
router = DefaultRouter()
router.register(r'newcustomers', NewCustomerViewSet)
router.register(r'underwriters', UnderwriterViewSet)
router.register(r'cashiers', CashierViewSet)
router.register(r'claimofficers', ClaimOfficerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('verify-new-customer/<int:customer_id>/', views.verify_new_customer, name='verify_new_customer'),
    path('submit_customer_data/', SubmitCustomerDataAPIView.as_view(), name='submit_customer_data'),
]
