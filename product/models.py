from django.db import models
from datetime import datetime
# Create your models here.


class Product(models.Model):
    Pro_Name = models.CharField(max_length=50)
    Pro_Descrebition = models.TextField (max_length= 15000)
    Pro_Price = models.DecimalField( max_digits=5, decimal_places=2)
    Pro_Cost = models.DecimalField (max_digits=5 , decimal_places=2)
    Pro_date = models.DateTimeField(default=datetime.now , blank=True)
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.Pro_Name