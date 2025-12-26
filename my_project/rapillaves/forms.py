from django import forms
from .models import Product, Proveedor, Operation
from decimal import Decimal

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
        fields = [ "product","quantity", "subtotal", "total"]
        widgets = {
            "subtotal" : forms.NumberInput(attrs={"readonly": True}),
            "total" : forms.NumberInput(attrs={"readonly": True})
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        
        if quantity > product.stock:
            raise forms.ValidationError(f"La cantidad '{quantity}' es mayor al stock actual, ingrese una cantidad menor")
        return quantity
    
    def save(self, commit = True):
        instance = super().save(commit=False)
        instance.operation_type = True
        
        price = instance.product.price
        quantity = instance.quantity
        product = instance.product
        
        instance.subtotal = price * instance.quantity
        instance.total = instance.subtotal * Decimal("1.13")
        
        product.stock -= quantity
        if commit:
            product.save()
            instance.save()
        return instance

class DevolutionForm(forms.ModelForm):
    class Meta:
        model = Operation
        fields = ["product","quantity","money_devolution","product_replacement","subtotal", "total"]
        widgets = {
            "subtotal" : forms.NumberInput(attrs={"readonly" : True, "id": "id_subtotal_devolution"}),
            "total" : forms.NumberInput(attrs={"readonly": True, "id": "id_total_devolution"}),
            "quantity" : forms.NumberInput(attrs={"id": "id_quantity_devolution"}),
            "money_devolution" : forms.CheckboxInput(),
            "product_replacement" : forms.CheckboxInput()
        }
    
    def clean_quantity(self):
        quantity = self.cleaned_data.get('quantity')
        product = self.cleaned_data.get('product')
        product_replacement = self.cleaned_data.get()("product_replacement")
        
        if product_replacement and quantity > product.stock:
            raise forms.ValidationError(f"La cantidad '{quantity}' es mayor al stock actual, ingrese una cantidad menor")
        return quantity
    
    def clean_devolution_option(self):
        money_devolution = self.cleaned_data.get("money_devolution")
        product_replacement = self.cleaned_data.get("product_replacement")
        
        if money_devolution and product_replacement:
            raise forms.ValidationError("No se puede seleccionar ambas opciones 'Devolucion de dinero' y 'reintegracion de producto' juntos")
        elif money_devolution == False or product_replacement == False:
            raise forms.ValidationError("Debe seleccionar una opcion de devolucion")
        return money_devolution, product_replacement

    
    def save(self, commit = True):
        instance =  super().save(commit = False)
        instance.operation_type = False
        
        price = instance.product.price
        quantity = instance.quantity
        product = instance.product
        money_devolution = instance.money_devolution
        product_replacement = instance.product_replacement
        
        if product_replacement :
            product.stock -= quantity
            instance.subtotal = 0
            instance.total = 0
        elif money_devolution :
            instance.subtotal = price * instance.quantity
            instance.total = instance.subtotal * Decimal("1.13")
        
        if commit :
            product.save()
            instance.save()
        return instance