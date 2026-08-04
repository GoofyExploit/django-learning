from django.shortcuts import render
from music.models import Music
# Create your views here.
def index(request):
    return render(request, 'music/index.html')

def songs(request):
    songs = Music.objects.all()
    context = {
        "songs" : songs
    }
    return render(request, 'music/songs.html', context)

def song(request, slug):
    song = Music.objects.get(slug=slug)
    context = {
        "song" : song
    }
    return render(request, 'music/details.html', context)

def genres(request):
    genres = Music.objects.values_list("genre", flat=True).distinct()
    context = {
        "genres" : genres,
    }
    return render(request, 'music/genres.html', context)

def genre(request, genre):
    songs = Music.objects.filter(genre__icontains=genre)
    context = {
        "songs" : songs,
        "genre" : genre
    }
    return render(request, 'music/genre.html', context)
