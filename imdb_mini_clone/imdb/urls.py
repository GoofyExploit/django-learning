from django.urls import path
from imdb import views

app_name = 'imdb'
urlpatterns = [
    path('', views.index, name="index"),
    path('movies/', views.movies, name="movies"),
    path('movies/genres/', views.genres, name="genres"),
    path('movies/actors/', views.actors, name="actors"),
    path('movies/directors/', views.directors, name="directors"),
    path('movies/years/', views.years, name="years"),
    path('movies/years/<int:year>/', views.year, name="year"),
    path('movies/directors/<str:director>/', views.director, name="director"),
    path('movies/actors/<str:actor>/', views.actor, name="actor"),
    path('movies/genres/<str:genre>/', views.genre, name="genre"),
    path('movies/<slug:slug>/', views.details, name="details")
]