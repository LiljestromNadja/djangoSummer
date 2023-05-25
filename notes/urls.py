from django.urls import path
from .views import *


urlpatterns = [
    
    path('', NoteListView.as_view()),

    path('note/<int:pk>/edit', NoteUpdateView.as_view()),
    path('note/add', NoteCreateView.as_view()),
    path('note/<int:pk>/delete', NoteDeleteView.as_view()),


]
