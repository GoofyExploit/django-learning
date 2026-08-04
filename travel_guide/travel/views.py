from django.shortcuts import render
from travel.models import Travel

# Create your views here.
def index(request):
    return render(request, 'travel/index.html')

def countries(request):
    countries = Travel.objects.values_list("country", flat=True).distinct()
    context = {
        "countries" : countries
    }
    return render(request, 'travel/countries.html', context)

def places(request, country):
    places = Travel.objects.filter(country__icontains=country)
    context = {
        "places" : places,
        "country" : country
    }
    return render(request, 'travel/places.html', context)

def place(request, country, slug):
    place = Travel.objects.get(slug=slug)
    context = {
        "place" : place,
        "country" : country
    }
    return render(request, 'travel/place.html', context)

def attractions(request):
    attractions = Travel.objects.all()
    context = {
        "attractions" : attractions
    }
    return render(request, 'travel/attractions.html', context)

def attraction(request, slug):
    attraction = Travel.objects.get(slug=slug)
    context = {
        "attraction" : attraction
    }
    return render(request, 'travel/attraction.html', context)