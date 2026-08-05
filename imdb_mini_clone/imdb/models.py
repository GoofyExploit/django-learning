from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    genre = models.CharField(max_length=200, blank=True)
    actor = models.CharField(max_length=200)
    director = models.CharField(max_length=200)
    year = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    runtime = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.title