from django.shortcuts import get_object_or_404

from rest_framework.viewsets import ViewSet
from rest_framework.views import APIView, Response
from rest_framework import status

from . import models, serializers




class ContactViewSet(ViewSet):
    
    def list(self, request):
        queryset = models.Contact.objects.all()
        serializer = serializers.ContactSerializer(instance=queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retreive(self, request, pk):
        query = get_object_or_404(models.Contact, id=pk)
        serializer = serializers.ContactSerializer(instance=query)
        return Response(serializer.data, status=status.HTTP_200_OK)