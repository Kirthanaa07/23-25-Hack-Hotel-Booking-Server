from django.db import models
from .room import Room


class Booking(models.Model):

    booking = models.CharField(max_length=50)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in = models.DateTimeField
    check_out = models.DateTimeField
    no_of_guests = models.IntegerField
    payment_type = models.CharField(max_length=50)
    total_amount = models.IntegerField