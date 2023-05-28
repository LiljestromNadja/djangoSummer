from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin #26.5
from django.contrib.auth.forms import UserCreationForm #28.5
from .models import *

class NoteBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'notes/base.html'

class NoteListView(LoginRequiredMixin, ListView):
    model = Note

class NoteUpdateView(UpdateView):
    model = Note
    fields = ["subject","message", "person"]
    success_url = '/'

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["subject","message", "person"]
    success_url = '/'

class NoteDeleteView(DeleteView):
    model = Note
    success_url = "/"

class PersonListView(LoginRequiredMixin, ListView):
    model = Person

#Muista ettei RegisterViewsiin laiteta LoginRequiredMixin koska muuten ei näy rekisteröitymättömälle käyttäjälle

class RegisterView(CreateView):
    form_class = UserCreationForm 
    template_name = "registration/register_form.html"
    success_url = "/"
#    success_message = "Created new user succesfully. You can now login"
