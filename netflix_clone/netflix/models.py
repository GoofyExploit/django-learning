from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    genre = models.CharField(max_length=200)
    actor = models.CharField(max_length=200)
    year = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.title