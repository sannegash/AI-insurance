from django.urls import path
from .views import TransferView

urlpatterns = [
    path('initiate-transfer/', TransferView.as_view(), name='initiate-transfer'),
]
