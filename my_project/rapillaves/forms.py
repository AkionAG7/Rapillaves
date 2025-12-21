from django import forms
from .models import Product, Proveedor, Operation

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ["name", "description", "price", "stock"]
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields= "__all__"
        
class SellRegisterForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["operation_type", "product","quantity","subtotal", "total"]

class DevolutionForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["operation_type", "product","quantity","money_devolution","product_replacement","subtotal", "total"]