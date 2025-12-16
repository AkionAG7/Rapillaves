from django.urls import path
from .views import show_inventory, show_proveedores, show_operation_options

urlpatterns = [
    path('inventario/', show_inventory, name='inventario'),
    path('proveedores/', show_proveedores, name='proveedores'),
    path('operations/', show_operation_options, name='operation_options')
]
