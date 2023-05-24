from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class BaseView(TemplateView):
    template_name = 'people/base.html'

class ContactListView(ListView):
    template_name = 'people/contact_list.html'
    model = Contact

class ContactUpdateView(UpdateView):
    model = Contact
    fields = ["fullname","nickname", "city"]
    success_url = '/'

class ContactCreateView(CreateView):
    model = Contact
    fields = ["fullname","nickname", "city"]
    success_url = '/'

class ContactDeleteView(DeleteView):
		model = Contact
		success_url = "/"














#class ContactListView(ListView):
#    template_name = 'people/contacts.html'


#class ContactListView(TemplateView):
#    template_name = 'people/contacts.html'
