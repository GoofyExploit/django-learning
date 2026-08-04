from django.shortcuts import render
from game.models import Game
# Create your views here.
def index(request):
    return render(request, 'game/index.html')

def games(request):
    games = Game.objects.all()
    context = {
        "games" : games
    }
    return render(request, 'game/games.html', context)

def details(request, slug):
    game = Game.objects.get(slug=slug)
    context = {
        "game" : game
    }
    return render(request, 'game/details.html', context)

def genres(request):
    genres = Game.objects.values_list("genre", flat=True).distinct()
    context = {
        "genres" : genres
    }
    return render(request, 'game/genres.html', context)

def genre(request, genre):
    game = Game.objects.filter(genre__icontains=genre)
    context = {
        "game": game,
        "genre" : genre
    }
    return render(request, 'game/genre.html', context)

def platforms(request):
    platforms = Game.objects.values_list("platform", flat=True).distinct()
    context = {
        "platforms" : platforms
    }
    return render(request, 'game/platforms.html', context)

def platform(request, platform):
    game = Game.objects.filter(platform__icontains=platform)
    context = {
        "game" : game, 
        "platform" : platform
    }
    return render(request, 'game/platform.html', context)