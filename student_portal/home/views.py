from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Welcome to Student Portal")

def about(request):
    return HttpResponse("This portal helps students manage courses.")