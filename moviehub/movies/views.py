from django.template.defaultfilters import title
from django.shortcuts import render
from movies.models import Movie
# Create your views here.
def index(request):
    movies = Movie.objects.all()
    context = {
        "movies" : movies
    }
    return render(request, "movies/index.html", context)

def about(request):
    return render(request, "movies/about.html")

def detail(request, slug):
    movie = Movie.objects.get(slug=slug)
    context = {
        "movie" : movie
    }
    return render(request, "movies/detail.html", context)