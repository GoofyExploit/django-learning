from student.views import StudentCreateView
from django.urls import path
from student.views import *
from student import views

app_name = 'student'
urlpatterns = [
    path('', StudentIndexView.as_view(), name="index"),
    path('about/', views.about, name = "about"),
    path('contact/', views.contact, name = "contact"),
    path('students/', StudentListView.as_view(), name="list"),
    path('students/add_student/', StudentCreateView.as_view(), name="create"),
    path('students/<slug:slug>/', StudentDetailView.as_view(), name="detail"),
    path('students/<slug:slug>/edit/', StudentUpdateView.as_view(), name="update"),
    path('students/<slug:slug>/delete/', StudentDeleteView.as_view(), name="delete")
]