from django.views.generic import TemplateView, ListView
from .models import *

class ContactListView(ListView):
    template_name = 'people/contacts.html'
    model = Contact











#class ContactListView(ListView):
#    template_name = 'people/contacts.html'


#class ContactListView(TemplateView):
#    template_name = 'people/contacts.html'
