#Täällä määritellään tämän apin urlit,luokkien määrittelyt views.py

from django.urls import path
from .views import *


urlpatterns = [
#    path('',BaseView.as_view()), #localhost:8000/
    path('', ContactListView.as_view()), #, localhost:8000/contactlist

    path('contact/<int:pk>/edit', ContactUpdateView.as_view()),
    path('contact/add', ContactCreateView.as_view()),
    path('contact/<int:pk>/delete', ContactDeleteView.as_view()),


    
   # path('contacts', ContactListView.as_view()), #localhost:8000/people/contacts

   
]
