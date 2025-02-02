from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt import views as jwt_views  # Import JWT views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('claims/', include('claims.urls')),
    path('policies/', include('policies.urls')),
    path('core/', include('core.urls')),
    path('risk/', include('risk.urls')),
    path('payment/', include('payment.urls')),
    path('vehicle/', include('vehicle.urls')),
    path('auth/', include('djoser.urls')),  # Djoser routes
    path('auth/jwt/', include('djoser.urls.jwt')),  # Djoser JWT routes
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),  # Simple JWT token obtain
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),  # Simple JWT token refresh
    path('chapa-webhook', include('django_chapa.urls'))
]
