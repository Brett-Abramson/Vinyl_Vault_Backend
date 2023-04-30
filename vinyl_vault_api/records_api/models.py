from django.db import models
import django_filters

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    tracks = models.IntegerField(blank=True)
    release_date = models.CharField(max_length=10, blank=True)
    artwork = models.CharField(max_length=255, blank=True) 
    spotify_id = models.CharField(max_length=24, blank=True)

class AlbumFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = Album
        fields = ['artist', 'title', 'release_date']