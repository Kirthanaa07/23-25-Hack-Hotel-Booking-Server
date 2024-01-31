from django.db import models

class Hotel(models.Model):
    name = models.CharField(max_length=75)
    images = models.CharField(max_length=200)
    address = models.CharField(max_length=75)
    city = models.CharField(max_length=50)
    amenities = models.CharField(max_length=200)
    rating = models.IntegerField()
    
