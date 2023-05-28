from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView #lisätty 26.5
from .views import *


urlpatterns = [

    
    path('', NoteBaseView.as_view()),
    
    path('listnotes', NoteListView.as_view()),

    path('note/<int:pk>/edit', NoteUpdateView.as_view()),
    path('note/add', NoteCreateView.as_view()),
    path('note/<int:pk>/delete', NoteDeleteView.as_view()),

    path('listpersons', PersonListView.as_view()),

    path('accounts/login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view(next_page="/")),
    path('register/', RegisterView.as_view()),
    
    


]
