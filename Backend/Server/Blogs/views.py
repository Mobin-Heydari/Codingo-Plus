from django.shortcuts import render, get_object_or_404
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import *

from .models import Blog, BlogSection
from .serializers import BlogSerializer, BlogSectionSerializer

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
        blog = get_object_or_404(Blog, pk=pk)
        
        # Serialize the specific blog instance
        serializer = BlogSerializer(blog)
        
        # Return the serialized data as a response
        return Response(serializer.data)