from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import AlbumSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Album
# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("artist")
    serializer_class = AlbumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['artist', 'title', 'release_date']
    search_fields = ['artist', 'title', 'release_date']

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("artist")
    serializer_class = AlbumSerializer