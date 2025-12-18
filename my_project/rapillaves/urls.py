from django.urls import path
from .views import show_inventory, show_proveedores, show_operation_options, create_inventory, update_inventory,show_product,create_proveedor, update_proveedores, show_proveedor

urlpatterns = [
    path('inventario/', show_inventory, name='inventario'),
    path('inventario/<int:pk>', show_product, name='producto'),
    path('inventario/create/', create_inventory, name='inventory_create'),
    path('inventario/update/<int:pk>/', update_inventory, name='inventory_update'),
    path('proveedores/', show_proveedores, name='proveedores'),
    path('proveedores/<int:pk>', show_proveedor, name='proveedor'),
    path('proveedores/create/', create_proveedor, name="proveedor_create"),
    path("/proveedores/update/<int:pk>/", update_proveedores, name="proveedor_update"),
    path('operaciones/', show_operation_options, name='operation_options')
]
