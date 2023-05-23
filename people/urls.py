#Täällä määritellään tämän apin urlit,luokkien määrittelyt views.py

from django.urls import path
from .views import *


urlpatterns = [
    path('', ContactListView.as_view()), #localhost:8000/people/

   # path('contacts', ContactListView.as_view()), #localhost:8000/people/contacts

   
]
