from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("new_music/", views.addNewMusic, name="add_music"),
]
