from django.shortcuts import render
from netflix.models import Movie

# Create your views here.
def index(request):
    return render(request, 'netflix/index.html')

def movies(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, 'netflix/movies.html', context)

def details(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        "movie" : movie
    }
    return render(request, 'netflix/details.html', context)

def genres(request):
    genres = Movie.objects.values_list("genre", flat=True).distinct()
    context = {
        "genres" : genres
    }
    return render(request, 'netflix/genres.html', context)

def genre(request, genre):
    movie = Movie.objects.filter(genre__icontains=genre)
    context = {
        "movie" : movie,
        "genre": genre
    }
    return render(request, 'netflix/genre.html', context)

def actors(request):
    actors = Movie.objects.values_list("actor", flat=True).distinct()
    context = {
        "actors" : actors
    }
    return render(request, 'netflix/actors.html', context)

def actor(request, actor):
    movie = Movie.objects.filter(actor__icontains=actor)
    context = {
        "movie" : movie,
        "actor" : actor
    }
    return render(request, 'netflix/actor.html', context)