from django.shortcuts import render
from journal.models import Journal
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from journal.form import JournalForm

# Create your views here.
class JournalIndexView(TemplateView):
    template_name = "journal/index.html"

def about(request):
    return render(request, 'journal/about.html')

def contact(request):
    return render(request, 'journal/contact.html')

class JournalListView(ListView):
    model = Journal
    template_name = 'journal/journal_list.html'
    context_object_name = "journals"

class JournalDetailView(DetailView):
    model = Journal
    template_name = 'journal/journal_detail.html'
    context_object_name = "journal"
    slug_field = "slug"
    slug_url_kwarg = "slug"

class JournalCreateView(CreateView):
    model = Journal
    form_class = JournalForm
    template_name = 'journal/journal_form.html'
    