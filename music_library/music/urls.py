from django.urls import path
from music import views

app_name = 'music'
urlpatterns = [
    path('', views.index, name="index"),
    path('songs', views.songs, name="songs"),
    path('songs/genres/', views.genres, name="genres"),
    path('songs/<slug:slug>/', views.song, name="song"),
    path('song/genres/<str:genre>/', views.genre, name="genre"),
]