from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.views import Response
from rest_framework import status


from .models import Project, Category
from .serializers import ProjectSerializer, CategorySerializer




class ProjectViewSet(ViewSet):
    
    # Method to list all projects
    def list(self, request):
        # Retrieve all Project objects from the database
        queryset = Project.objects.all()
        # Serialize the queryset into a format suitable for the response
        serializer = ProjectSerializer(instance=queryset, many=True)
        # Return the serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to retrieve a specific project by its slug
    def retrieve(self, request, pk):
        # Retrieve all Project objects from the database
        queryset = Project.objects.all()
        # Get the specific project object or return a 404 error if not found
        project = get_object_or_404(queryset, slug=pk)
        # Serialize the specific project object
        serializer = ProjectSerializer(instance=project)
        # Return the serialized project data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class CategoryViewSet(ViewSet):
    
    # Method to list all categories
    def list(self, request):
        # Retrieve all categories objects from the database
        queryset = Category.objects.all()
        # Serialize the queryset into a format suitable for the response
        serializer = CategorySerializer(instance=queryset, many=True)
        # Return the serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Method to retrieve a specific category by its slug
    def retrieve(self, request, pk):
        # Retrieve all Category objects from the database
        queryset = Category.objects.all()
        # Get the specific category object or return a 404 error if not found
        category = get_object_or_404(queryset, slug=pk)
        # Serialize the specific category object
        serializer = CategorySerializer(instance=category)
        # Return the serialized category data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)