from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HackHotelBookingapi.models import Hotel

class HotelView(ViewSet):
    """Hotel View"""
    
    def retrieve(self, request, pk):
      try:
        hotel = Hotel.objects.get(pk=pk)
        serializer = HotelSerializer(hotel)
        return Response(serializer.data)
      except Hotel.DoesNotExist as ex:
        return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
      
    def list(self, request):
      hotels = Hotel.objects.all()
      serializer = HotelSerializer(hotels, many=True)
      return Response(serializer.data)
    
    def create(self, request):
        hotel = Hotel.objects.create(
            name = request.data["name"],
            images = request.data["images"],
            address = request.data["address"],
            city = request.data["city"],
            amenities = request.data["amenities"],
            rating = request.data["rating"]
        )
        serializer = HotelSerializer(hotel)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      
    def update(self, request, pk):
      hotel = Hotel.objects.get(pk=pk)
      hotel.name = request.data["name"]
      hotel.images = request.data["images"]
      hotel.address = request.data["address"]
      hotel.city = request.data["city"]
      hotel.amenities = request.data["amenities"]
      hotel.rating = request.data["rating"]
      hotel.save()
      
      return Response(None, status=status.HTTP_204_NO_CONTENT)
        
class HotelSerializer(serializers.ModelSerializer):
    class Meta:
      model = Hotel
      fields = ('id', 'name', 'images', 'address', 'city', 'amenities', 'rating')   
