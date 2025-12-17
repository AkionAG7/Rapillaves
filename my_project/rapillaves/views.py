from django.shortcuts import render,redirect, get_object_or_404
from .models import Product, Proveedor
from .forms import ProductForm

def show_inventory(request):
    productos = Product.objects.all()
    form = ProductForm()
    context = {"productos" : productos, "form": form, "edit_mode" : False, "show_mode": False}
    return render(request ,'inventory/inventory.html', context)

def show_product(request, pk):
    productos = Product.objects.all()
    producto = get_object_or_404(Product, pk = pk)
    return render(request, "inventory/inventory.html",{
        "productos" : productos,
        "form": ProductForm(instance=producto),
        "edit_mode" : False,
        "show_mode" : True,
        "producto" : producto
    })

def create_inventory(request):
    if request.method == "POST":
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("inventario")

def update_inventory(request, pk):
    producto = get_object_or_404(Product, pk = pk)
    
    if request.method == "POST" :
        form = ProductForm(request.POST, instance= producto)
        if form.is_valid():
            form.save()
            return redirect("inventario")
    else:
        form = ProductForm(instance=producto)
    productos = Product.objects.all()
    return render(request, "inventory/inventory.html",{
        "productos" : productos,
        "form" : form,
        "edit_mode" : True,
        "show_mode" : False,
        "producto" : producto
    })

def show_proveedores(request):
    proveedores = Proveedor.objects.all()
    context = {"proveedores": proveedores}
    return render(request, "inventory/proveedor.html", context)

def show_operation_options(request):
    return render(request, "operations/options.html")
