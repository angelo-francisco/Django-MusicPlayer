from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("user/", include("users.urls")),
    path("", RedirectView.as_view(permanent=False, url="/music/")),
    path("music", include("music.urls")),
]
