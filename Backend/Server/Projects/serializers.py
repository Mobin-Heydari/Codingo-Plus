from rest_framework import serializers
from .models import Project, Category




class ProjectSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Project
        fields = "__all__"
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"