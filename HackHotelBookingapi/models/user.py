from django.db import models

class User(models.Model):
    uid = models.CharField(max_length=50)
    first_name = models.CharField(max_length=75)
    last_name = models.CharField(max_length=75)
    email = models.CharField(max_length=75)
    bio = models.CharField(max_length=100)
