from django.urls import path
from netflix import views

app_name = "netflix"
urlpatterns = [
    path("", views.index, name="index"),
    path("movies/", views.movies, name="movies"),
    path("movies/genres/", views.genres, name="genres"),
    path("movies/actors/", views.actors, name="actors"),
    path("movies/actors/<str:actor>/", views.actor, name="actor"),
    path("movies/<slug:slug>/", views.details, name="details"),
    path("movies/genres/<str:genre>/", views.genre, name="genre"),
]
