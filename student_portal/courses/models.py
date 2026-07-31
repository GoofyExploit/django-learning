from django.db import models
from students.models import Student

# Create your models here.
class Course(models.Model):
    course_name = models.CharField(max_length=200)
    course_code = models.CharField(max_length=10)
    credit = models.IntegerField()
    created_date = models.DateTimeField("Date of Creation")
    def __str__(self):
        return self.course_name

class Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    grade = models.CharField(max_length=3)
    active = models.BooleanField("Student Status")
    def __str__(self):
        return f"{self.student} --> {self.course}"
