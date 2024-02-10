"""View module for handling requests about game types"""
from http import HTTPMethod
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import serializers, status
from HackHotelBookingapi.models import Booking, User, Room
from HackHotelBookingapi.views.room_view import RoomSerializer


class BookingView(ViewSet):
    def retrieve(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def list(self, request):
        
        userId = request.GET.get('userId')
        if userId is not None:
            bookings = Booking.objects.filter(user_id=userId)
        else:
            bookings = Booking.objects.all()
                
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def create(self, request):
        user = User.objects.get(pk=request.data["user_id"])
        room = Room.objects.get(pk=request.data["room_id"])

        booking = Booking.objects.create(
            no_of_guests=request.data["no_of_guests"],
            check_in=request.data["check_in"],
            check_out=request.data["check_out"],
            total_amount=request.data["total_amount"],
            payment_type=request.data["payment_type"],
            user=user,
            room=room,
        )
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    def update(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.no_of_guests = request.data["no_of_guests"]
        booking. check_in = request.data["check_in"]
        booking.check_out = request.data["check_out"]
        booking.total_amount = request.data["total_amount"]
        booking.payment_type = request.data["payment_type"]
        booking.save()
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
    
    def destroy(self, request, pk):
        booking = Booking.objects.get(pk=pk)
        booking.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
class BookingSerializer(serializers.ModelSerializer):
    room = RoomSerializer()
    class Meta:
        model = Booking
        fields = (
            "id",
            "user",
            "room",
            "no_of_guests",
            "check_in",
            "check_out",
            "total_amount",
            "payment_type",
        )
