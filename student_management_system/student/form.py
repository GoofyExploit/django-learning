from django.template.defaultfilters import slugify
from django.forms import ModelForm
from student.models import Student


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["slug"]


class StudentUpdateForm(ModelForm):
    class Meta:
        model = Student
        fields = "__all__"
        exclude = ["slug"]
