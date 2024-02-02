"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HackHotelBookingapi.models import Room


class RoomView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)


    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)
      
class RoomSerializer(serializers.ModelSerializer):
    """JSON serializer for game types
    """
    class Meta:
        model = Room
        fields = ('id', 'hotel', 'room_number', 'room_type', 'images', 'price_per_night')      
