from django.shortcuts import render
from .models import Product

def show_inventory(request):
    productos = Product.objects.all()
    context = {"productos" : productos}
    return render(request ,'inventory/inventory.html', context)
