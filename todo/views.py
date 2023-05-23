#Luokkien määrittely
from django.views.generic import TemplateView, ListView
from .models import *


class HelloView(TemplateView):
    template_name='todo/hello.html'

class ToinenView(TemplateView):
    template_name = 'todo/toinen.html'

class BaseView(TemplateView):
    template_name = 'todo/base.html'

class TaskListView(ListView):
    model = Task


