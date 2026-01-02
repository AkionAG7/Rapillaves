from django.shortcuts import render,redirect, get_object_or_404
from .models import Product, Proveedor, Operation
from .forms import ProductForm, ProveedorForm, SellRegisterForm,DevolutionForm
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils.timezone import now
from datetime import datetime

# VISTAS PARA PRODUCTOS Y SI INVENTARIADO
def show_inventory(request):
    search = request.GET.get("search", "")
    productos = Product.objects.all()
    form = ProductForm()
    
    if search:
        productos = productos.filter(
            Q(name__icontains=search)
        )
    paginator = Paginator(productos, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"productos" : page_obj, "form": form, "edit_mode" : False, "show_mode": False}
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
    
def change_inventory_status(request, pk):
    if request.method == "POST":
        product = get_object_or_404(Product, pk = pk)
        product.status = not product.status
        product.save()
    return redirect("inventario")

#Vistas para los proveedores
def show_proveedores(request):
    search = request.GET.get("search", "")
    proveedores = Proveedor.objects.all()
    form = ProveedorForm()
    if search:
        proveedores = proveedores.filter(
            Q(name__icontains=search)
        )
    paginator = Paginator(proveedores, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    context = {"proveedores": page_obj, "form": form, "edit_mode": False, "show_mode": False}
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

def change_proveedor_status(request, pk):
    if request.method == "POST":
        proveedor = get_object_or_404(Proveedor, pk = pk)
        proveedor.status = not proveedor.status
        proveedor.save()
    return redirect("proveedores")

#Vistas para las operaciones
def show_operations(request):
    operations = Operation.objects.all()
    
    start_date = request.GET.get("start_date")
    end_date = request.GET.get("end_date")
    
    if start_date and not end_date:
        operations = operations.filter(
            created_at__date__gte=start_date
        )
    elif end_date and not start_date:
        operations = operations.filter(
            created_at__date__lte=end_date
        )
    elif start_date and end_date:
        operations = operations.filter(
            created_at__date__range=[start_date, end_date]
        )
    paginator = Paginator(operations, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    
    form_sell = SellRegisterForm()
    form_devolution = DevolutionForm()
    context = {"operations": page_obj,"sell": form_sell, "devolution":form_devolution ,"show_mode" : False}
    return render(request, "operations/operations.html", context)

def show_operation(request, pk):
    operations = Operation.objects.all()
    operation = get_object_or_404(Operation, pk=pk)
    context = {
        "operations": operations,
        "operation": operation,
        "show_mode": True
    }
    return render(request, "operations/operations.html", context)

def SellRegister(request):
    form_sell = SellRegisterForm()
    if request.method == "POST":
        form_sell = SellRegisterForm(request.POST)
        if form_sell.is_valid():
            form_sell.save()
            return redirect("operations")
    context = {"operations": Operation.objects.all(),"sell": form_sell,
            "devolution":DevolutionForm() ,"show_mode" : False}
    return render(request, "operations/operations.html", context)

def DevolutionRegister(request):
    form_devolution = DevolutionForm()
    if request.method == "POST":
        form_devolution = DevolutionForm(request.POST)
        if form_devolution.is_valid():
            form_devolution.save()
            return redirect("operations")
    context = {"operations": Operation.objects.all(),"sell": SellRegisterForm(),
            "devolution":form_devolution ,"show_mode" : False}
    return render(request, "operations/operations.html", context)


