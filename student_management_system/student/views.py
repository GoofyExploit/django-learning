from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, CreateView, DeleteView, TemplateView
from student.models import Student
from student.form import StudentForm, StudentUpdateForm
from django.utils.text import slugify
# Create your views here.

class StudentIndexView(TemplateView):
    template_name = 'student/index.html'

def about(request):
    return render(request, 'student/about.html')

def contact(request):
    return render(request, 'student/contact.html')

class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'student/student_form.html'

    # To override the slug field to populate the slug automatically
    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.name)
        return super().form_valid(form)

class StudentListView(ListView):
    model = Student
    template_name = 'student/student_list.html'
    context_object_name = 'students'

class StudentDetailView(DetailView):
    model = Student
    template_name = 'student/student_detail.html'
    context_object_name = 'student'

class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentUpdateForm
    template_name = 'student/student_form.html'

class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'student/confirm.html'
    success_url = reverse_lazy('student:list')