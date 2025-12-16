from django.urls import path
from .views import show_inventory, show_proveedores

urlpatterns = [
    path('inventario/', show_inventory, name='inventario'),
    path('proveedores/', show_proveedores, name='proveedores')
]
