from django.shortcuts import render
from .models import Product, Proveedor

def show_inventory(request):
    productos = Product.objects.all()
    context = {"productos" : productos}
    return render(request ,'inventory/inventory.html', context)

def show_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {"proveedores": proveedores}
    return render(request, "inventory/proveedor.html", context)
