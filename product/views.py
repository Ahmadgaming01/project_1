from django.shortcuts import render , redirect
from .models import Item
# Create your views here.


def New_item(request):
    Product = Item.objects.all()
    return render (request , 'product/home.html' , {'items':Product})

def details_item(request ,item_id):
    item = Item.objects.get(id=item_id)
    return render (request , 'product/details.html' ,{'item':item})
