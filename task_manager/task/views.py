from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from task.models import Task
from task.form import TaskForm

# Create your views here.
class HomeView(TemplateView):
    model = Task
    template_name = 'task/index.html'

class TaskListView(ListView):
    model = Task
    template_name = 'task/task_list.html'
    context_object_name = "tasks"

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task/task_detail.html'
    context_object_name = "task"

class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task/form.html'
    success_url = reverse_lazy('task:list')