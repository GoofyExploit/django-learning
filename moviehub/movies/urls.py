from django.urls import path
from movies import views

app_name = "movies"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("<slug:slug>/", views.detail, name="detail")
]