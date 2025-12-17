from django.urls import path
from .views import show_inventory, show_proveedores, show_operation_options, create_inventory, update_inventory,show_product

urlpatterns = [
    path('inventario/', show_inventory, name='inventario'),
    path('inventario/<int:pk>', show_product, name='producto'),
    path('inventario/create/', create_inventory, name='inventory_create'),
    path('inventario/update/<int:pk>/', update_inventory, name='inventory_update'),
    path('proveedores/', show_proveedores, name='proveedores'),
    path('operaciones/', show_operation_options, name='operation_options')
]
