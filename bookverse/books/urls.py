from django.urls import path
from books import views

app_name = "books"
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('books/genres/', views.genre, name="genre"),
    path('books/<slug:slug>/', views.detail, name="detail"),
    path('books/genres/<str:genre>/', views.category, name="category")
]