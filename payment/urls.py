from django.urls import path
from .views import MakePaymentView

urlpatterns = [
    path('make-payment/', MakePaymentView.as_view(), name='make-payment'),
]
