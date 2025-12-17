from django import forms
from .models import Product, Proveedor

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields= ["name", "description", "price", "stock"]
        
class ProveedorForm(forms.ModelForm):
    class Meta:
        model = Proveedor
        fields= "__all__"