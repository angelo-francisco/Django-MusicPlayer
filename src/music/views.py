from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Song


@login_required()
def home(request):
    if request.method == "GET":
        songs = Song.objects.all()
        context = {
            'songs': songs,
        }
        return render(request, "pages/music/home.html", context=context)
    else: ...


@login_required()
def addNewMusic(request):
    if request.method == "GET":
        return redirect('/music/#my_modal_8')
    else: 
        song = Song.objects.create(
            name=request.POST['music-name'],
            description=request.POST['music-description'],
            singer=request.POST['music-singer'],
            banner=request.FILES['music-banner'],
            song_file=request.FILES['music-file'],
            user=request.user,
        )

        song.save()
        messages.success(request, 'Nova música adicionada!')
        return redirect(reverse('home'))

