from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewCustomerViewSet, UnderwriterViewSet, CashierViewSet, ClaimOfficerViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'newcustomers', NewCustomerViewSet)
router.register(r'underwriters', UnderwriterViewSet)
router.register(r'cashiers', CashierViewSet)
router.register(r'claimofficers', ClaimOfficerViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]