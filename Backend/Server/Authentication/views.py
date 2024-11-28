from django.contrib.auth import authenticate, login, logout

from rest_framework.views import APIView, Response
from rest_framework import status 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import OneTimePassword




class TokenObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainSerializer



class UserLoginAPIView(APIView):
    
    def post(self, request):
        # we need to check if user is authenticated or not for having better security and user experience
        if request.user.is_authenticated == False:
            # Validate the request data
            serializer = serializers.UserLoginSerializer(data=request.data)
            if serializer.is_valid():
                email = serializer.validated_data['email']
                password = serializer.validated_data['password']
                
                # Authenticate the user
                user = authenticate(username=email, password=password)
                if user is not None:
                    # Generate tokens
                    refresh = RefreshToken.for_user(user)
                    
                    # Return the tokens in the response
                    return Response({
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }, status=status.HTTP_200_OK)
                else:
                    return Response({'detail': 'Invalid data.'}, status=status.HTTP_401_UNAUTHORIZED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'You are authenticated.'}, status=status.HTTP_403_FORBIDDEN)