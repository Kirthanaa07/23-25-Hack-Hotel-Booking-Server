"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from HackHotelBookingapi.models import Booking, User, Room


class BookingView(ViewSet):
    """Level up game types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        booking = Booking.objects.get(pk=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
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


class BookingSerializer(serializers.ModelSerializer):
    """JSON serializer for game types"""

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
