from django.urls import path
from recipebook  import views 

app_name = 'recipebook'
urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('recipes/', views.recipe, name="recipe"),
    path('recipes/categories/', views.categories, name="categories"),
    path('recipes/categories/<str:category>/', views.category, name="category"),
    path('recipes/<slug:slug>/', views.detail, name='detail')
]