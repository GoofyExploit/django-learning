from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    author = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    published_year = models.IntegerField()
    pages = models.IntegerField()
    rating = models.DecimalField(decimal_places=2, max_digits=3)
    description = models.TextField()

    def __str__(self):
        return self.title