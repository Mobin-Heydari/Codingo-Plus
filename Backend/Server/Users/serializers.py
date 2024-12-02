# Import necessary modules from Django REST Framework
from rest_framework import serializers

# Import the User model from the current application
from .models import User

# Import profile models
from Profiles.models import EmployeeProfile, CustomersProfile




# Define a serializer for the User model
class UserSerializer(serializers.ModelSerializer):
    
    # Define a custom field to include the user's profile data
    profile = serializers.SerializerMethodField()
    
    # Meta class to define model and fields to be serialized
    class Meta:
        model = User  # Specify the model to serialize
        fields = ('id', 'user_type', 'username', 'email', 'joined_date', 'profile')  # Specify the fields to include in the serialized output
        
    
    # Method to retrieve the profile data based on user type
    def get_profile(self, obj):
        from Profiles.serializers import EmployeeProfileSerializer, CustomersProfileSerializer
        try:
            # Check the user_type to determine which profile to retrieve
            if obj.user_type == 'CST':
                # Retrieve the CustomersProfile associated with the user
                profile = CustomersProfile.objects.get(customer=obj)
                # Serialize the profile data using the appropriate serializer
                serializer = CustomersProfileSerializer(instance=profile)
                
            elif obj.user_type == 'EMP':
                # Retrieve the EmployeeProfile associated with the user
                profile = EmployeeProfile.objects.get(employee=obj)
                # Serialize the profile data using the appropriate serializer
                serializer = EmployeeProfileSerializer(instance=profile)
            
            else:
                # Return None or raise an exception for unknown user types
                return None  # or raise an exception for unknown user_type
                
        except (CustomersProfile.DoesNotExist, EmployeeProfile.DoesNotExist):
            # Return None if the profile does not exist
            return None  # or handle the error accordingly
        except Exception as e:
            # Handle other potential exceptions that may arise
            return None  # or raise an exception or log the error
        
        # Return the serialized profile data
        return serializer.data