from django.forms import ModelForm
from notes.models import Note

class NotesForm(ModelForm):
    class Meta:
        model = Note
        fields = "__all__"