from django.urls import path
from .views import show_inventory, show_proveedores, show_operation_options, create_inventory

urlpatterns = [
    path('inventario/', show_inventory, name='inventario'),
    path('inventario/create/', create_inventory, name='inventory_create'),
    path('proveedores/', show_proveedores, name='proveedores'),
    path('operaciones/', show_operation_options, name='operation_options')
]
