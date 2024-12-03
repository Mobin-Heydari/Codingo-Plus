from rest_framework import serializers

from .models import Contact



class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        # Specify the model that this serializer will work with
        model = Contact
        # Indicate that all fields from the Contact model should be included in the serializer
        fields = "__all__"
        
    def create(self, validated_data):
        # Create a new Contact object using the validated data provided
        return Contact.objects.create(**validated_data)