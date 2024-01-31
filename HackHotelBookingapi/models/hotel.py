from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=75)
    images = models.JSONField(blank=True, null=True)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    amenities = models.TextField(max_length=2000)
    rating = models.IntegerField()
