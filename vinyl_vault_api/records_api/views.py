from django.shortcuts import render
from rest_framework import generics
from .serializers import AlbumSerializer
from .models import Album
# Create your views here.

class AlbumList(generics.ListCreateAPIView):
    queryset = Album.objects.all().order_by("artist")
    serializer_class = AlbumSerializer

class AlbumDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Album.objects.all().order_by("artist")
    serializer_class = AlbumSerializer