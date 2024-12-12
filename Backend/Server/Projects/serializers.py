from rest_framework import serializers
from .models import Project, Category
from Server.settings import ALLOWED_HOSTS



class ProjectSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()
    class Meta:
        model = Project
        fields = "__all__"
        
    def get_image_url(self, obj):
        image = str(obj.image)
        if ALLOWED_HOSTS == []:
            path_host = "http://127.0.0.1:8000"
        else:
            path_host = ALLOWED_HOSTS[0]
        image_url = f"{path_host}/media/{image}"
        return image_url
        
        
        
class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = "__all__"