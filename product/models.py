from django.db import models
from datetime import datetime
# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=50)
    pro_details = models.TextField (max_length= 15000)
    image = models.ImageField(upload_to='Items/', blank=True)
    price = models.IntegerField()
    category = models.CharField(max_length=50)
    def __str__(self):
        return self.name