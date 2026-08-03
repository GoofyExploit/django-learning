from django.shortcuts import render
from books.models import Book


# Create your views here.
def index(request):
    books = Book.objects.all()
    context = {"books": books}
    return render(request, "books/index.html", context)


def detail(request, slug):
    book = Book.objects.get(slug=slug)
    context = {"book": book}
    return render(request, "books/detail.html", context)


def about(request):
    return render(request, "books/about.html")


def genre(request):
    genres = Book.objects.values_list("genre", flat=True).distinct()
    context = {
        "genres": genres,
    }
    return render(request, "books/genre.html", context)

def category(request, genre):
    books = Book.objects.filter(genre__iexact=genre)
    context = {
        "books" : books,
        "genre" : genre
    }
    return render(request, 'books/category.html', context)
