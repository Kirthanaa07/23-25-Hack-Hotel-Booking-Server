from django.db import models
from .hotel import Hotel


class Room(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    images= models.JSONField(blank=True, null=True)
    room_number = models.IntegerField()
    room_type = models.CharField(max_length=50)
    price_per_night = models.IntegerField()