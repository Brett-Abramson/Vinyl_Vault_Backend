from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    year_released = models.IntegerField()
