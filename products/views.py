from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import *

class BaseView(TemplateView): 
    template_name = 'products/base.html'

class ProductListView(ListView):
    model = Product

class ProductUpdateView(UpdateView):
    model = Product
    fields = ["name","description", "price"]
    success_url = '/'
    
class ProductCreateView(CreateView):
    model = Product
    fields = ["name","description", "price"]
    success_url = '/'

class ProductDeleteView(DeleteView):
		model = Product
		success_url = "/"

