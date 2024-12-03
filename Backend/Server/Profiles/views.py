from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import SimpleUserProfile, EmployeeProfile
from .serializers import SimpleUserProfileSerializer, EmployeeProfileSerializer

from Users.models import User



class EmployeeProfileViewSet(ViewSet):
    
    # Method to handle GET requests for listing all employees
    def list(self, request):
        # Retrieve all EmployeeProfile objects from the database
        employees = EmployeeProfile.objects.all()
        # Serialize the employee data, allowing for multiple employee instances
        serializer = EmployeeProfileSerializer(employees, many=True)
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle GET requests for retrieving a specific employee by employee
    def retrieve(self, request, pk):
        # Use get_object_or_404 to fetch the EmployeeProfile instance or return a 404 error if not found
        employee = get_object_or_404(EmployeeProfile, employee__username=pk)
        # Serialize the retrieved employee instance
        serializer = EmployeeProfileSerializer(instance=employee)
        # Return the serialized employee data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle PUT/PATCH requests for updating a specific employee
    def update(self, request, pk):
        employee = get_object_or_404(EmployeeProfile, employee__username=pk)
        
        serializer = EmployeeProfileSerializer(instance=employee, data=request.data, partial=True)  # Use partial=True for PATCH
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SimpleUserProfileViewSet(ViewSet):
    
    # Method to handle GET requests for listing all profiles
    def list(self, request):
        # Retrieve all SimpleUserProfile objects from the database
        profiles = SimpleUserProfile.objects.all()
        # Serialize the user data, allowing for multiple user instances
        serializer = SimpleUserProfileSerializer(profiles, many=True)
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle GET requests for retrieving a specific profile by user
    def retrieve(self, request, pk):
        # Use get_object_or_404 to fetch the SimpleUserProfile instance or return a 404 error if not found
        user = get_object_or_404(SimpleUserProfile, user__username=pk)
        # Seruserialize the retrieved user instance
        serializer = SimpleUserProfileSerializer(instance=user)
        # Return the serialized user data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle PUT/PATCH requests for updating a specific user
    def update(self, request, pk):
        user = get_object_or_404(SimpleUserProfile, user__username=pk)
        serializer = SimpleUserProfileSerializer(instance=user, data=request.data, partial=True)  # Use partial=True for PATCH
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)