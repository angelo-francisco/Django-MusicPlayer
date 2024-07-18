from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(permanent=False, url="/user/login")),
    path("login/", views._login, name="login"),
    path("signup/", views._signup, name="signup"),
    path("logout/", views._logout, name="logout"),
]
