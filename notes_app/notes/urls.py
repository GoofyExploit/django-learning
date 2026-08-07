from notes import views
from notes.views import *
from django.urls import path

app_name = 'notes'
urlpatterns = [
    path('', NotesIndexView.as_view(), name = "index"),
    path('notes/', NotesListView.as_view(), name="list"),
    path('notes/new/', NotesCreateView.as_view(), name="create"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('notes/<slug:slug>/', NotesDetailView.as_view(), name="detail"),
    path('notes/<slug:slug>/edit/', NotesUpdateView.as_view(), name="update"),
    path('notes/<slug:slug>/delete/', views.NotesDeleteView, name="delete")
]