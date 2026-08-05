from django.urls import path
from feedback.views import *

app_name = 'feedback'
urlpatterns = [
    path('', FeedbackListView.as_view(), name="list"),
    path('new/', FeedbackCreateView.as_view(), name="create"),
    path('<slug:slug>/', FeedbackDetailView.as_view(), name="detail"),
]