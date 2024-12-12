from rest_framework import serializers
from .models import Project, Category
from Server.settings import ALLOWED_HOSTS



class ProjectSerializer(serializers.ModelSerializer):
    # SerializerMethodField to get the image URL
    image_url = serializers.SerializerMethodField()
    
    # SerializerMethodField to get the category name
    category = serializers.SerializerMethodField()
    
    class Meta:
        model = Project  # Specify the model to serialize
        fields = "__all__"  # Include all fields from the model
        
    def get_image_url(self, obj):
        # Convert the image field to a string
        image = str(obj.image)
        
        # Determine the host URL based on ALLOWED_HOSTS
        if ALLOWED_HOSTS == []:
            path_host = "http://127.0.0.1:8000"  # Localhost if no hosts are allowed
        else:
            path_host = ALLOWED_HOSTS[0]  # Use the first allowed host
        
        # Construct the full image URL
        image_url = f"{path_host}/media/{image}"
        return image_url  # Return the constructed image URL
    
    def get_category(self, obj):
        # Return the category name associated with the project
        return obj.category.category
    

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category  # Specify the model to serialize
        fields = "__all__"  # Include all fields from the model