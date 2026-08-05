from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from feedback.models import Feedback
from feedback.forms import FeedbackForm

# Create your views here.
class FeedbackListView(ListView):
    model = Feedback
    context_object_name = "feedbacks"

class FeedbackDetailView(DetailView):
    model = Feedback
    context_object_name = "feedback"

class FeedbackCreateView(CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback/forms.html"
    success_url = reverse_lazy("feedback:list")