from rest_framework import serializers

from .models import Blog, BlogSection, Category



# Serializer for the Blog model
class BlogSerializer(serializers.ModelSerializer):
    
    # Define a custom field 'sections' that will use a method to get its value
    sections = serializers.SerializerMethodField()
    
    # will be used to display the categories of the blog
    category = serializers.SerializerMethodField()
    
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
        


# Serializer for the BlogSection model
class BlogSectionSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = BlogSection  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the BlogSection model
        

class CategorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category  # Specify the model to serialize
        fields = '__all__'  # Include all fields from the Category model