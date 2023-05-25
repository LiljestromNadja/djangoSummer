from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)    
    apartment = models.CharField(max_length=100, null=True)  
    email = models.EmailField(null=True, blank=True)  

    
    def __str__(self):

        return self.name

class Note(models.Model):
    subject = models.CharField(max_length=100)
    message = models.TextField(max_length=500)
    person = models.ForeignKey(Person, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f" {self.subject} {self.person}"
    
        #return self.subject


