from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500, null=True )
    price = models.FloatField(blank=True,null=True)
#    created = models.DateTimeField(auto_now_add=True, null=True)
#    brand = models.ForeignKey(Brandi, on_delete=models.CASCADE, null=True, blank=True)
   
    def __str__(self):
        return self.name

