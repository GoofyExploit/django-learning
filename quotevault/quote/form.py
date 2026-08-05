from django.forms import ModelForm
from quote.models import Quote

class QuoteForm(ModelForm):
    class Meta:
        model = Quote
        fields = "__all__"