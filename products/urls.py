from django.urls import path
from .views import *


urlpatterns = [
    
    path('', ProductListView.as_view()),

    path('product/<int:pk>/edit', ProductUpdateView.as_view()),
    path('product/add', ProductCreateView.as_view()),
    path('product/<int:pk>/delete', ProductDeleteView.as_view()),


]
