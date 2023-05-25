from django.contrib import admin
from django.urls import path, include 


urlpatterns = [
    path('admin/', admin.site.urls), #admin-urlit
    path('todo/', include('todo.urls')), #todo-apin urlit, esim http://localhost:8000/todo/toinen
    path('people/', include('people.urls')),

    path("product/", include('products.urls')),
    path("", include('notes.urls')),
   
]
