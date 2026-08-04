from django.utils import duration
from django.db import models

# Create your models here.
class Music(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    artist = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    album = models.CharField(max_length=200)
    duration=models.CharField(max_length=4)
    release_year = models.CharField(max_length=200)
    lyrics_preview = models.TextField()
    
    def __str__(self):
        return self.title