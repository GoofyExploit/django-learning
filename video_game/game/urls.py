from django.urls import path
from game import views

app_name = 'game'
urlpatterns = [
    path('', views.index, name="index"),
    path('games/', views.games, name="games"),
    path('games/genres/', views.genres, name="genres"),
    path('games/genres/<str:genre>/', views.genre, name="genre"),
    path('game/platforms/', views.platforms, name="platforms"),
    path('game/platforms/<str:platform>/', views.platform, name="platform"),
    path('games/<slug:slug>/', views.details, name="details"),
]