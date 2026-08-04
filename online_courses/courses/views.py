from django.shortcuts import render
from courses.models import Course

# Create your views here.
def index(request):
    return render(request, 'courses/index.html')

def courses(request):
    courses = Course.objects.all()
    context = {
        "courses" : courses
    }
    return render(request, 'courses/courses.html', context)

def details(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        "course" : course
    }
    return render(request, 'courses/details.html', context)

def categories(request):
    categories = Course.objects.values_list("category", flat=True).distinct()
    context = {
        "categories" : categories
    }
    return render(request, 'courses/categories.html', context)

def category(request, category):
    course = Course.objects.filter(category__icontains=category)
    context = {
        "course" : course,
        "category" : category
    }
    return render(request, 'courses/category.html', context)

def instructors(request):
    instructors = Course.objects.values_list("instructor", flat=True)
    context = {
        "instructors" : instructors
    }
    return render(request, 'courses/instructors.html', context)

def instruct_course(request, instructor):
    courses = Course.objects.filter(instructor__icontains=instructor)
    context = {
        "courses" : courses,
        "instructor" : instructor
    }
    return render(request, 'courses/instruct_course.html', context)

def course(request, slug):
    course = Course.objects.get(slug=slug)
    context = {
        "course" : course
    }
    return render(request, 'courses/course.html', context)