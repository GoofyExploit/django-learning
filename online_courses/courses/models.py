from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    category = models.CharField(max_length=200)
    instructor = models.CharField(max_length=200)
    duration = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    description = models.TextField()

    def __str__(self):
        return self.title