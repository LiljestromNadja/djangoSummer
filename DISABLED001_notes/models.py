from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)    

    
    def __str__(self):

        return self.name

class Note(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, related_name="notes")

    
    def __str__(self):
        #return f" {self.subject} {self.person}"
    
        return self.subject



#reverse relation
#person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

