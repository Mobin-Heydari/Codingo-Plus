from django.contrib.auth import authenticate, login, logout
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView, Response
from rest_framework import status 

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from . import serializers
from .models import OneTimePassword
from .permissions import IsNotAuthenticated




class TokenObtainView(TokenObtainPairView):
    serializer_class = serializers.TokenObtainSerializer



class UserLoginAPIView(APIView):
    # we need to check if user is authenticated or not for having better security and user experience
    permission_classes = [IsNotAuthenticated]
    
    def post(self, request):
        # Using serializers to get the email and password from the request body
        serializer = serializers.UserLoginSerializer(data=request.data)
        # Validating the data
        if serializer.is_valid():
            # Catching
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
    

class UserRegisterAPIView(APIView):
    
    """
    API View for user registration
    """
    
    # Check if the user is not already authenticated
    permission_classes = [IsNotAuthenticated]
    
    def post(self, request, token):
        
        # Get the OneTimePassword object from the database using the provided token
        otp = get_object_or_404(OneTimePassword, token=token)
        
        if otp:
            # Serialize the request data using the UserRegisterSerializer
            serializer = serializers.RegisterSerializer(data=request.data, context={'otp_token' : otp.token})
            if serializer.is_valid(raise_exception=True):
                # Saving the user data and getting user and tokens
                user_data = serializer.create(validated_data=serializer.validated_data, token=token)

                # Return a success response with user data and tokens
                return Response(
                    {
                        'Detail': {
                            'Message': 'User  created successfully',
                            'User': user_data['user'],
                            'Token': user_data['tokens']
                        }
                    }, status=status.HTTP_201_CREATED
                )  
            else:
                # Return an error response if the serializer is invalid
                return Response(
                    {'Detail': serializer.errors},
                    status=status.HTTP_400_BAD_REQUEST
                )
        else:
            # Return an error response if the OTP does not exist
            return Response(
                {'Detail': 'OTP does not exist'},
                status=status.HTTP_404_NOT_FOUND
            )


class OneTimePasswordAPIView(APIView):
    """
        API view to generate a one-time password 
    """
    
    # Check if the user is not already authenticated
    permission_classes = [IsNotAuthenticated]
    
    def post(self, request):
        """
        Handle POST request for one-time password auth
        """
        # Create an instance of the serializer with the request data
        serializer = serializers.OneTimePasswordSerializer(data=request.data)
        
        # Validate the serializer data
        if serializer.is_valid(raise_exception=True):
            # Call the create method with the validated data
            otp_data = serializer.create(validated_data=serializer.validated_data)  # Save and get the OTP data
            
            # Return a success response with the OTP details
            return Response(
                {
                    'Detail': {
                        'Message': 'Otp created successfully',
                        'token': otp_data['token'],  # Assuming otp_data has a token attribute
                        'code': otp_data['code']       # Assuming otp_data has a code attribute
                    }
                }, status=status.HTTP_201_CREATED
            )
        else:
            # Return an error response if the serializer validation fails
            return Response({'Detail': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
