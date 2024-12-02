from django.shortcuts import get_object_or_404

from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import CustomersProfile, EmployeeProfile
from .serializers import CustomersProfileSerializer, EmployeeProfileSerializer

from Users.models import User



class EmployeeViewSet(ViewSet):
    
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


class CustomerViewSet(ViewSet):
    
    # Method to handle GET requests for listing all customers
    def list(self, request):
        # Retrieve all CustomersProfile objects from the database
        customers = CustomersProfile.objects.all()
        # Serialize the customer data, allowing for multiple customer instances
        serializer = CustomersProfileSerializer(customers, many=True)
        # Return the serialized data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle GET requests for retrieving a specific customer by customer
    def retrieve(self, request, pk):
        # Use get_object_or_404 to fetch the CustomersProfile instance or return a 404 error if not found
        customer = get_object_or_404(CustomersProfile, customer__username=pk)
        # Serialize the retrieved customer instance
        serializer = CustomersProfileSerializer(instance=customer)
        # Return the serialized customer data as a response
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to handle PUT/PATCH requests for updating a specific customer
    def update(self, request, pk):
        customer = get_object_or_404(CustomersProfile, customer__username=pk)
        serializer = CustomersProfileSerializer(instance=customer, data=request.data, partial=True)  # Use partial=True for PATCH
        if serializer.is_valid():
            serializer.save()  # Save the updated instance
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)