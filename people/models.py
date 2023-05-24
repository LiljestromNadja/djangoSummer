from django.db import models

class Contact(models.Model):
    fullname = models.CharField(max_length=150)
    nickname = models.CharField(unique = True, max_length=150)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
#    city = models.TextField(max_length=100)


    def __str__(self):
        return self.fullname

    
#        return f"{self.fullname} {self.city}"
    
    
