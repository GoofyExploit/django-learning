from django.urls import path
from courses import views

app_name='courses'
urlpatterns = [
    path('', views.index, name="index"),
    path('courses/', views.courses, name="courses"),
    path('categories/', views.categories, name="categories"),
    path('instructors/', views.instructors, name="instructors"),
    path('instructors/<str:instructor>/', views.instruct_course, name="instruct_course"),
    path('instructors/courses/<slug:slug>/', views.course, name="course"),
    path('categories/<str:category>/', views.category, name="category"),
    path('courses/<slug:slug>/', views.details, name="details"),
]