from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer





class TokenObtainSerializer(TokenObtainPairSerializer):
    # Custom Token Obtain Serializer that inherits from TokenObtainPairSerializer
    
    @classmethod
    def get_token(cls, user):
        # Override the get_token method to add custom claims to the token
        
        # Call the parent class's get_token method to get the default token
        token = super().get_token(user)
        
        # Add custom claims to the token
        # User custom claims
        token['username'] = user.username  # Add the user's username to the token
        token['email'] = user.email  # Add the user's email to the token
        token['user_type'] = user.user_type  # Add the user's type to the token
        token['joined_date'] = str(user.joined_date)  # Add the user's joined date to the token
        
        # Return the token with the added custom claims
        return token



class UserLoginSerializer(serializers.Serializer):
    
    email = serializers.EmailField(required=True)
    
    password = serializers.CharField(write_only=True, required=True)
    