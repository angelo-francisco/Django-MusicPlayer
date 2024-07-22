from django.db import models
from django.contrib.auth.models import User


class Song(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    singer = models.CharField(max_length=50)
    banner = models.FileField(upload_to="banner/")
    song_file = models.FileField(upload_to="music/")
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class RecentMusic(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)

class PlayList(models.Model):
    name = models.CharField(max_length=50)
    song = models.ForeignKey(Song, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self) -> str:
        return self.name