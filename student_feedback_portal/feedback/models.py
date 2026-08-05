from unicodedata import decimal
from django.db import models

# Create your models here.
class Feedback(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    student = models.CharField(max_length=200)
    rating = models.DecimalField(max_digits=3, decimal_places=1)
    message = models.TextField()

    def __str__(self):
        return self.title