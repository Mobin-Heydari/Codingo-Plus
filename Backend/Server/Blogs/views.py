from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.status import *

from .models import Blog, BlogSection, Category
from .serializers import BlogSerializer, BlogSectionSerializer, CategorySerializer




# ViewSet for handling Blog-related requests
class BlogViewSet(ViewSet):
    
    # Method to handle GET requests for listing all blogs
    def list(self, request):
        # Retrieve all Blog instances from the database
        blogs = Blog.objects.all()
        
        # Serialize the blog instances using the BlogSerializer
        serializer = BlogSerializer(blogs, many=True)
        
        # Return the serialized data as a response
        return Response(serializer.data)
    
    # Method to handle GET requests for retrieving a specific blog by its primary key (pk)
    def retrieve(self, request, pk):
        # Fetch the Blog instance or return a 404 error if not found
        blog = get_object_or_404(Blog, pk=slug)
        
        # Serialize the specific blog instance
        serializer = BlogSerializer(blog)
        
        # Return the serialized data as a response
        return Response(serializer.data)



class CategoryListAPIView(APIView):
    
    def get(self, request):
        # Get all queryset
        queryset = Category.objects.all()
        # Serializing these queries
        serializer = CategorySerializer(queryset, many=True)
        # Returning the response
        return Response(serializer.data)
    


class CategoryDetailAPIView(APIView):
    
    def get(self, request, slug):
        # Get all query
        query = get_object_or_404(Category, slug=slug)
        # Serializing the query
        serializer = CategorySerializer(query)
        # Returning the response
        return Response(serializer.data)