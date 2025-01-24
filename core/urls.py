# core/urls.py
from django.urls import path
from core.views import UserSignupView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import SignInView
urlpatterns = [
    path('signin/', SignInView.as_view(), name='signin'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', UserSignupView.as_view(), name='signup'),
]