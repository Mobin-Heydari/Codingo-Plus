# Import necessary modules and functions
from django.shortcuts import get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.views import Response 
from rest_framework import status 

# Import the User model and UserSerializer
from .models import User
from .serializers import UserSerializer



# Define a ViewSet for User-related operations
class UserViewSet(ViewSet):
    
    # Method to handle GET requests for listing all users
    def list(self, request):
        # Retrieve all User objects from the database
        users = User.objects.all()
        # Serialize the user data, allowing for multiple user instances
        serializer = UserSerializer(users, many=True)
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle GET requests for retrieving a specific user by username
    def retrieve(self, request, pk):
        # Use get_object_or_404 to fetch the User instance or return a 404 error if not found
        user = get_object_or_404(User, username=pk)
        # Serialize the retrieved user instance
        serializer = UserSerializer(instance=user)
        # Return the serialized user data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)