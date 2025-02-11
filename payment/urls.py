from django.urls import path
from .views import home, transfer
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('transfer/', views.transfer, name='transfer')
]
