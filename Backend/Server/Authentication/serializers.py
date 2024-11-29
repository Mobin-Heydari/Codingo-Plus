from django.contrib.auth.password_validation import validate_password

from rest_framework import serializers
from rest_framework import validators

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from Users.models import User




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
    
    

class RegisterSerializer(serializers.Serializer):
    """
    Serializer for user registration
    """
    
    # Email field with unique validator to ensure email is not already in use
    email = serializers.EmailField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    # Username field with unique validator to ensure username is not already in use
    username = serializers.CharField(
        validators=[
            validators.UniqueValidator(queryset=User.objects.all())
        ]
    )
    
    # Password field with custom validator and write-only access
    password = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True
    )

    # Password confirmation field with write-only access
    password_conf = serializers.CharField(
        validators=[validate_password],
        write_only=True,
        required=True
    )
    
    
    def validate(self, attrs):
        """
        Validate the serializer data
        """
        # Check if the password and password confirmation match
        if attrs['password'] == attrs['password_conf']:
            # Check if the password length is between 8 and 16 characters
            if len(attrs['password']) >= 8 and len(attrs['password']) <= 16:
                return attrs
            else:
                raise serializers.ValidationError({"Detail": "Password length should be between 8 to 16 characters."})
        else:
            raise serializers.ValidationError({"Detail": "Passwords fields didn't match."})
        
    

    def create(self, validated_data):
        """
        Create a new user instance
        """
        # Create a new user instance with the validated data
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            user_type="CST"
        )
        user.save()
        return user
    