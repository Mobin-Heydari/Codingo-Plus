from rest_framework import serializers

from .models import Blog, BlogSection, Category
from Server.settings import ALLOWED_HOSTS


# Serializer for the Blog model
class BlogSerializer(serializers.ModelSerializer):
    
    # Define a custom field 'sections' that will use a method to get its value
    sections = serializers.SerializerMethodField()
    
    # will be used to display the categories of the blog
    category = serializers.SerializerMethodField()
    
    # will be used to return the image full url for frontend
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the Blog model

    # Method to get the serialized data for the related BlogSection instances
    def get_sections(self, obj):
        # Create a serializer instance for the related sections
        serializer = BlogSectionSerializer(instance=obj.sections, many=True)
        
        # Return the serialized data for the sections
        return serializer.data

    def get_category(self, obj):
        #  Returning only category name 
        return obj.category.category 
    
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
        


# Serializer for the BlogSection model
class BlogSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogSection  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the BlogSection model
        

class CategorySerializer(serializers.ModelSerializer):
    
    image_url = serializers.SerializerMethodField()
    
    class Meta:
        model = Category  # Specify the model to serialize
        fields = ['id', 'category', 'slug', 'image_url']
        
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