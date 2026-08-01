from django.shortcuts import render

# Create your views here.
def index(request):
    context = {
        "heading" : "Welcome to MoviesHub",
        "owner": "Lucky",
        "year": 2026,
        "logged_in": True,
        "movies": [
            "Interstellar", "Inception", "The Dark Knight"
        ]
    }
    return render(request, "movies/index.html", context)

def about(request):
    return render(request, "movies/about.html")