from django.db import models

# Create your models here.
class Game(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    genre = models.CharField(max_length=200)
    platform = models.CharField(max_length=200)
    developer = models.CharField(max_length=200)
    release_year = models.CharField(max_length=200)
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    description = models.TextField()
    
    def __str__(self):
        return self.title