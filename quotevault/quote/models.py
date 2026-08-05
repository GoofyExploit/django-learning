from django.db import models

# Create your models here.
class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.quote