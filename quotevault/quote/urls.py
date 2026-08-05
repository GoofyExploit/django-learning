from quote.views import QuoteCreateView
from quote.views import QuoteListView
from django.urls import path
from quote.views import *

app_name = "quote"
urlpatterns = [
    path('', QuoteListView.as_view(), name="list"),
    path('new_form/', QuoteCreateView.as_view(), name = "create"),
    path('<slug:slug>/', QuoteDetailView.as_view(), name="detail"),
]