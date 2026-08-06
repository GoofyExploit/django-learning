from django.db import models
from django.urls import reverse
# Create your models here.
class Journal(models.Model):
    title = models.CharField(max_length=200)
    mood = models.CharField(max_length=200)
    entry = models.TextField()
    date = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("journal:detail", kwargs = {"slug" : self.slug})