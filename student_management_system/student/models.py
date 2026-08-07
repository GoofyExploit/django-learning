from django.urls import reverse
from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    course = models.CharField(max_length=200)
    year = models.IntegerField()
    email = models.EmailField()
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('student:detail' , kwargs = {"slug" : self.slug})