from django.contrib import admin
from .models import Product,Proveedor,Product_Provedor,Operation
admin.site.register(Product)
admin.site.register(Proveedor)
admin.site.register(Product_Provedor)
admin.site.register(Operation)