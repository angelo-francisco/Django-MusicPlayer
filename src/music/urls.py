from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new_music/", views.addNewMusic, name="add_music"),
    path("info/<int:id>/", views.infoMusic, name="info_music"),
    path("play/<int:id>/", views.playMusic, name="play_music"),
    path("playlists/", views.playlists, name="playlists")
]
