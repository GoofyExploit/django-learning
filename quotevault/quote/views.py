from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from quote.models import Quote
from quote import form

# Create your views here.
class QuoteListView(ListView):
    model = Quote
    template_name = 'quote/quote_list.html' 
    context_object_name = "quotes"

class QuoteDetailView(DetailView):
    model = Quote
    template_name = 'quote/quote_detail.html'
    context_object_name = "quote"

class QuoteCreateView(CreateView):
    model = Quote
    form_class = form.QuoteForm
    template_name = 'quote/form.html'
    success_url = reverse_lazy("quote:list")