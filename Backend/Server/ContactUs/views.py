from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView, Response
from rest_framework import status

from . import models, serializers




class ContactViewSet(ViewSet):
    
    # Handles GET requests to list all contacts
    def list(self, request):
        # Retrieve all contact objects from the database
        queryset = models.Contact.objects.all()
        # Serialize the queryset to convert it into a format suitable for the response
        serializer = serializers.ContactSerializer(instance=queryset, many=True)
        # Return the serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handles GET requests to retrieve a specific contact by its primary key (pk)
    def retrieve(self, request, pk):
        # Get the contact object or return a 404 error if not found
        query = get_object_or_404(models.Contact, id=pk)
        # Serialize the single contact object
        serializer = serializers.ContactSerializer(instance=query)
        # Return the serialized data with a 200 OK status
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    # Handles POST requests to create a new contact
    def create(self, request):
        # Initialize the serializer with the incoming data
        serializer = serializers.ContactSerializer(data=request.data)
        # Validate the data; if invalid, raise an exception
        if serializer.is_valid(raise_exception=True):
            # Save the new contact object to the database
            serializer.save()
            # Return a success message along with the serialized data and a 201 Created status
            return Response(
                {
                    "Detail": "Contact created successfully",
                    "contact": serializer.data
                },
                status=status.HTTP_201_CREATED
            )
        else:
            # If the serializer is not valid, return the errors with a 400 Bad Request status
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)