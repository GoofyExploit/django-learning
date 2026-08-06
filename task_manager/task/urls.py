from task.views import HomeView
from task.views import *
from django.urls import path

app_name = "task"
urlpatterns = [
    path('', HomeView.as_view(), name = "index"),
    path('tasks/', TaskListView.as_view(), name="list"),
    path('tasks/new_task/', TaskCreateView.as_view(), name="create"),
    path('tasks/<slug:slug>/', TaskDetailView.as_view(), name = "detail"),
]   