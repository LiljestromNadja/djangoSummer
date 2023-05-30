from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin#26.5, 30-5
from django.contrib.auth.forms import UserCreationForm #28.5, 
#from django.contrib.messages.views import SuccessMessageMixin #30.5
from .models import *

class NoteBaseView(LoginRequiredMixin, TemplateView):
    template_name = 'notes/base.html'

class NoteListView(LoginRequiredMixin, ListView):
    model = Note

# user sees only users own notes
#    	def get_queryset(self):
#		return Task.objects.filter(owner__username=self.request.user)

class NoteUpdateView(UserPassesTestMixin, UpdateView):
    model = Note
    fields = ["subject","message", "category"]
    success_url = '/'

    def test_func(self):
        object = self.get_object()
        return self.request.user == object.owner

class NoteCreateView(LoginRequiredMixin, CreateView):
    model = Note
    fields = ["subject","message", "category"]
    success_url = '/'

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class NoteDeleteView(UserPassesTestMixin, DeleteView):
    model = Note
    success_url = "/"

    def test_func(self):
    	object = self.get_object()
    	return self.request.user == object.owner

class CategoryListView(LoginRequiredMixin, ListView):
    model = Category

#Muista ettei RegisterViewsiin laiteta LoginRequiredMixin jos sen halutaan näkyvän rekisteröitymättömälle käyttäjälle

class RegisterView(LoginRequiredMixin, CreateView):
    form_class = UserCreationForm 
    template_name = "registration/register_form.html"
    success_url = "/"
#    success_message = "Created new user succesfully. You can now login"
