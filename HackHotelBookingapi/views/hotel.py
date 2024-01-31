from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HackHotelBookingapi.models import Hotel

class HotelView(ViewSet):
    """Hotel View"""
    
    def retrieve(self, request, pk):
        """Handle GET requests for single hotel
        Returns:
            Response -- JSON serialized hotel post
        """
        try:
          hotel = Hotel.objects.get(pk=pk)
          serializer = HotelSerializer(hotel)
          return Response(serializer.data)
        except Hotel.DoesNotExist as ex:
          return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
      model = Hotel
      fields = ('id', )   
