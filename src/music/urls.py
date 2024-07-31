from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new_music/", views.addNewMusic, name="add_music"),
    path("info/<int:id>/", views.infoMusic, name="info_music"),
    path("play/<int:id>/", views.playMusic, name="play_music"),
    path("playlists/", views.playlists, name="playlists"),
    path("add_playlist/<int:id>", views.add_music_playlist, name="add_playlist"),
    path("add_music_playlist/", views.add_effective, name="add_effective"),
    path("delete_playlist/<int:id>", views.delete_playlist, name="delete_playlist")
]
