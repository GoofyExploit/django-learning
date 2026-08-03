from django.shortcuts import render
from recipebook.models import Recipe
# Create your views here.
def index(request):
    return render(request, 'recipebook/index.html')

def about(request):
    return render(request, 'recipebook/about.html')

def recipe(request):
    recipes = Recipe.objects.all()
    context = {
        "recipes" : recipes
    }
    return render(request, 'recipebook/recipe.html', context)

def categories(request):
    categories = Recipe.objects.values_list("category", flat=True).distinct()
    context = {
        'categories' : categories
    }
    return render(request, 'recipebook/categories.html', context)

def category(request, category):
    recipes = Recipe.objects.filter(category__iexact=category)
    context = {
        "recipes": recipes,
        "category" : category
    }
    return render(request, 'recipebook/category.html', context)

def detail(request, slug):
    recipe = Recipe.objects.get(slug=slug)
    context = {
        "recipe" : recipe
    }
    return render(request, 'recipebook/detail.html', context)