from rest_framework import serializers
from .models import Album

class AlbumSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = ("id", "artist", "title", "tracks", "release_date", "artwork", "spotify_id")