from django.urls import path
from courses import views

urlpatterns = [
    path("courses/", views.courses, name = "courses"),
    path("courses/python/", views.python_course, name = "python course"),
    path("courses/django/", views.django_course, name = "django course"),
    path("courses/javascript/", views.js_course, name = "javascript course")
]