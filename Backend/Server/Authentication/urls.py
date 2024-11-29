from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView

from . import views



app_name = "Authentication"


urlpatterns = [
    # Tokens 
    path('token/', views.TokenObtainView.as_view(), name="token_obtain"),
    path('refresh-token/', TokenRefreshView.as_view(), name="token_refresh"),
    
    # User Login
    path('login/', views.UserLoginAPIView.as_view(), name="user_login"),
    
    # User Registeration
    path('registeration/', views.UserRegisterAPIView.as_view(), name="user_registeration"),
]
