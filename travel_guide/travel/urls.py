from django.urls import path
from travel import views

app_name = "travel"
urlpatterns = [
    path("", views.index, name="index"),
    path("countries/", views.countries, name="countries"),
    path('attractions/', views.attractions, name="attractions"),
    path('attractions/<slug:slug>/', views.attraction, name="attraction"),
    path("countries/<str:country>/", views.places, name="places"),
    path('countries/<str:country>/<slug:slug>/', views.place, name="place")
]