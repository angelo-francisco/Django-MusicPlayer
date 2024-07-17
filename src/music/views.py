from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required


@login_required()
def home(request):
    return render(request, "pages/music/home.html")

