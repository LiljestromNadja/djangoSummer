#Täällä määritellään tämän apin urlit,luokkien määrittelyt views.py

from django.urls import path
from .views import *


urlpatterns = [
    path('', TaskListView.as_view()), #http://localhost:8000/todo/
    #path('about', HelloView.as_view)
    path('hello', HelloView.as_view()),
    path('toinen', ToinenView.as_view()),
    path('base', BaseView.as_view()),

   
]
