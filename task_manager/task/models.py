from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    priority = models.CharField(max_length=200)
    due_date = models.DateField()
    slug = models.SlugField()

    def __str__(self):
        return self.title