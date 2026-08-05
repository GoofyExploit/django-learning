from django.shortcuts import render
from imdb.models import Movie

# Create your views here.
def index(request):
    return render(request, 'imdb/index.html')

def movies(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, 'imdb/movies.html', context)

def details(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        "movie" : movie
    }
    return render(request, 'imdb/details.html', context)

def genres(request):
    genres = Movie.objects.values_list("genre", flat=True).distinct()
    context = {
        "genres" : genres
    }
    return render(request, 'imdb/genres.html', context)

def genre(request, genre):
    movie = Movie.objects.filter(genre__icontains=genre)
    context = {
        "movie" : movie,
        "genre" : genre
    }
    return render(request, 'imdb/genre.html', context)

def actors(request):
    actors = Movie.objects.values_list("actor", flat=True).distinct()
    context = {
        "actors" : actors
    }
    return render(request, 'imdb/actors.html', context)

def actor(request, actor):
    movie = Movie.objects.filter(actor__icontains=actor)
    context = {
        "movie": movie,
        "actor" : actor
    }
    return render(request, 'imdb/actor.html', context)

def directors(request):
    directors = Movie.objects.values_list("director", flat=True).distinct()
    context = {
        "directors" : directors
    }
    return render(request, 'imdb/directors.html', context)

def director(request, director):
    movie = Movie.objects.filter(director__icontains=director)
    context = {
        "director" : director,
        "movie" : movie
    }
    return render(request, 'imdb/director.html', context)

def years(request):
    years = Movie.objects.values_list("year", flat=True).distinct()
    context = {
        "years" : years
    }
    return render(request, 'imdb/years.html', context)

def year(request, year):
    movie = Movie.objects.filter(year__icontains=year)
    context = {
        "movie" : movie,
        "year" : year
    }
    return render(request, 'imdb/year.html', context)