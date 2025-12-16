from django.shortcuts import render,redirect
from .models import Product, Proveedor
from .forms import ProductForm

def show_inventory(request):
    productos = Product.objects.all()
    form = ProductForm()
    context = {"productos" : productos, "form": form}
    return render(request ,'inventory/inventory.html', context)

def create_inventory(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("inventario")

def show_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {"proveedores": proveedores}
    return render(request, "inventory/proveedor.html", context)

def show_operation_options(request):
    return render(request, "operations/options.html")
