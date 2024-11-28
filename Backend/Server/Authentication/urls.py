from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views



app_name = "Authentication"


urlpatterns = [
    # Tokens 
    path('token/', views.TokenObtainView.as_view(), name="token_obtain"),
    path('refresh-token/', TokenRefreshView.as_view(), name="token_refresh"),
]
