from django.urls import path
from students import views

urlpatterns = [
    path("students/", views.students, name= "students"),
    path("students/register/", views.register, name = "student register"),
    path("students/login/", views.login, name = "student login")
]