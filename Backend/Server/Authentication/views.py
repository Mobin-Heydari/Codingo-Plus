from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView, Response
from rest_framework import status 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import OneTimePassword




class TokenObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainSerializer
