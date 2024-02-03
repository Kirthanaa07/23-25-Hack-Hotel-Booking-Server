"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HackHotelBookingapi.models import Room, Hotel


class RoomView(ViewSet):
    def retrieve(self, request, pk):
        room = Room.objects.get(pk=pk)
        serializer = RoomSerializer(room)
        return Response(serializer.data)

    def list(self, request):
        room = Room.objects.all()
        serializer = RoomSerializer(room, many=True)
        return Response(serializer.data)

    def create(self, request):
        hotel = Hotel.objects.get(pk=request.data["hotel_id"])

        room = Room.objects.create(
            room_number=request.data["room_number"],
            images=request.data["images"],
            price_per_night=request.data["price_per_night"],
            room_type=request.data["room_type"],
            hotel=hotel,
        )
        serializer = RoomSerializer(room)
        return Response(serializer.data)
    
    def update(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.room_number = request.data["room_number"]
        room.images = request.data["images"]
        room.price_per_night = request.data["price_per_night"]
        room.room_type = request.data["room_type"]
        room.save()

        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        room = Room.objects.get(pk=pk)
        room.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
        


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = (
            "id",
            "hotel",
            "room_number",
            "room_type",
            "images",
            "price_per_night",
        )
