from django.urls import path
from . import views

urlpatterns = [
    path("api/albums", views.AlbumList.as_view(), name="album_list"),
    path("api/albums/<int:pk>", views.AlbumDetail.as_view(), name="album_detail"),
]