from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from notes.models import Note
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from notes.form import NotesForm

# Create your views here.
class NotesIndexView(TemplateView):
    template_name = 'notes/index.html'

class NotesListView(ListView):
    model = Note
    template_name = 'notes/notes_list.html'
    context_object_name = 'notes'

class NotesDetailView(DetailView):
    model = Note
    template_name = 'notes/notes_detail.html'
    context_object_name = 'note'

# def NotesCreateView(request):
#     if request.method == 'POST':
#         form = NotesForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('notes:list')
#     else:
#         form = NotesForm()
#     return render(request, 'notes/notes_form.html', {"form" : form})

class NotesCreateView(CreateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes/notes_form.html' 

# def NotesUpdateView(request, slug):
#     note = Note.objects.get(slug=slug)
#     if request.method == 'POST':
#         form = NotesForm(request.POST, instance=note)
#         if form.is_valid():
#             form.save()
#             return redirect(note)
#     else:
#         form = NotesForm(instance=note)
#     return render(request, 'notes/notes_form.html', {"form" : form})

class NotesUpdateView(UpdateView):
    model = Note
    form_class = NotesForm
    template_name = 'notes/notes_form.html'

# class NotesDeleteView(DeleteView):
#     model = Note
#     template_name = 'notes/notes_delete_confirm.html'
#     success_url = reverse_lazy('notes:list')

def NotesDeleteView(request, slug):
    note = Note.objects.get(slug=slug)
    if request.method == 'POST':
        note.delete()
        return redirect('notes:list')
    return render(request, 'notes/notes_delete_confirm.html', {"note" : note})

def about(request):
    return render(request, 'notes/about.html')

def contact(request):
    return render(request, 'notes/contact.html')