from enum import unique
from unicodedata import decimal
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, null=True)
    year = models.IntegerField("Release Year")
    director = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    plot = models.TextField()

    def __str__(self):
        return self.title