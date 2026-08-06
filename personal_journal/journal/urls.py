from journal.views import *
from django.urls import path

app_name = 'journal'
urlpatterns = [
    path('', JournalIndexView.as_view(), name="index"),
    path('journals/', JournalListView.as_view(), name="list"),
    path('journals/new_entry/', JournalCreateView.as_view(), name="create"),
    path('journals/<slug:slug>/', JournalDetailView.as_view(), name="detail")
]