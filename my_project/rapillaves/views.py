from django.shortcuts import render,redirect, get_object_or_404
from .models import Product, Proveedor, Operation
from .forms import ProductForm, ProveedorForm, SellRegisterForm,DevolutionForm

# VISTAS PARA PRODUCTOS Y SI INVENTARIADO
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

#Vistas para los proveedores
def show_proveedores(request):
    proveedores = Proveedor.objects.all()
    form = ProveedorForm()
    context = {"proveedores": proveedores, "form": form, "edit_mode": False, "show_mode": False}
    return render(request, "inventory/proveedor.html", context)

def show_proveedor(request, pk):
    proveedores= Proveedor.objects.all()
    proveedor = get_object_or_404(Proveedor, pk = pk)
    context= {"proveedores": proveedores,
            "proveedor": proveedor,
            "form": ProveedorForm(instance= proveedor),
            "edit_mode": False,
            "show_mode": True}
    return render(request,"inventory/proveedor.html",context )

def create_proveedor(request):
    if request.method == "POST":
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
    return redirect("proveedores")

def update_proveedores(request, pk):
    proveedor = get_object_or_404(Proveedor, pk = pk)
    if request.method == "POST":
        form = ProveedorForm(request.POST, instance=proveedor)
        if form.is_valid():
            form.save()
            return redirect("proveedores")
    else:
        form = ProveedorForm(instance=proveedor)
    proveedores = Proveedor.objects.all()
    context ={
        "proveedores": proveedores,
        "proveedor" :proveedor,
        "form": form,
        "edit_mode": True,
        "show_mode": False
    }
    return render(request,"inventory/proveedor.html", context)

#Vistas para las operaciones
def show_operations(request):
    operations = Operation.objects.all()
    form_sell = SellRegisterForm()
    form_devolution = DevolutionForm()
    context = {"operations": operations,"sell": form_sell, "devolution":form_devolution ,"show_mode" : False}
    return render(request, "operations/operations.html", context)

def SellRegister(request):
    if request.method == "POST":
        form_sell = SellRegisterForm(request.POST)
        if form_sell.is_valid():
            form_sell.save()
            return redirect("operations")
    context = {"operations": Operation.objects.all(),"sell": form_sell,
            "devolution":DevolutionForm() ,"show_mode" : False}
    return render(request, "operations/operations.html", context)

def DevolutionRegister(request):
    if request.method == "POST":
        form_devolution = DevolutionForm(request.POST)
        if form_devolution.is_valid():
            form_devolution.save()
            return redirect("operations")
    context = {"operations": Operation.objects.all(),"sell": SellRegisterForm(),
            "devolution":form_devolution ,"show_mode" : False}
    return render(request, "operations/operations.html", context)


