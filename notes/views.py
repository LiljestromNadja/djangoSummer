from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class NoteBaseView(TemplateView):
    template_name = 'notes/base.html'

class NoteListView(ListView):
    model = Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ["subject","message", "person"]
    success_url = '/'

class NoteCreateView(CreateView):
    model = Note
    fields = ["subject","message", "person"]
    success_url = '/'

class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/"
