from django.db import models
from .hotel import Hotel


class Room(models.Model):

    room = models.CharField(max_length=50)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    image_url = models.CharField(max_length=50)
    room_number = models.IntegerField
    room_type = models.CharField(max_length=50)
    price_per_night = models.IntegerField