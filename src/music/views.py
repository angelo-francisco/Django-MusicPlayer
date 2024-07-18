from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.core.serializers import json
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

def infoMusic(request, id):
    if request.method == "GET":
        song = get_object_or_404(Song, id=id)
        request.session['song_name'] = song.name
        request.session['song_description'] = song.description
        request.session['song_banner'] = song.banner.url if song.banner else ''
        request.session['song_created_at'] = song.created_at.strftime('%d/%m/%Y')
        request.session['song_singer'] = song.singer
        request.session['song_user'] = song.user.username if song.user else ''

        return redirect('/music/#my_modal_9')

def playMusic(request, id):
    if request.method == "GET":
        song = get_object_or_404(Song, id=id)
        request.session['song_name'] = song.name
        request.session['song_banner'] = song.banner.url if song.banner else ''
        request.session['song_file'] = song.song_file.url
        request.session['song_singer'] = song.singer

        return redirect('/music/#my_modal_10')