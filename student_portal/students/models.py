from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=200)
    roll_number = models.IntegerField()
    email = models.CharField(max_length=200)
    admission_date = models.DateTimeField("Admission Date")
    def __str__(self):
        return self.full_name