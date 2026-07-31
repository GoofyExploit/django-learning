from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def courses(request):
    return HttpResponse("Courses Home")

def python_course(request):
    return HttpResponse("Python Course")

def django_course(request):
    return HttpResponse("Django Course")

def js_course(request):
    return HttpResponse("JavaScript Course")