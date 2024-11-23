from rest_framework import serializers

from .models import Blog, BlogSection



# Serializer for the Blog model
class BlogSerializer(serializers.ModelSerializer):
    
    # Define a custom field 'sections' that will use a method to get its value
    sections = serializers.SerializerMethodField()
    
    class Meta:
        model = Blog  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the Blog model

    # Method to get the serialized data for the related BlogSection instances
    def get_sections(self, obj):
        # Create a serializer instance for the related sections
        serializer = BlogSectionSerializer(instance=obj.sections, many=True)
        
        # Return the serialized data for the sections
        return serializer.data
        


# Serializer for the BlogSection model
class BlogSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogSection  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the BlogSection model