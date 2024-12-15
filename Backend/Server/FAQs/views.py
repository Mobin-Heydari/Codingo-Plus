from rest_framework.views import APIView, Response
from rest_framework.status import *

from . import serializers, models



class FaqAPIView(APIView):
    
    def get(self, request):
        queryset = models.FAQ.objects.all()
        serializer = serializers.FAQSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)