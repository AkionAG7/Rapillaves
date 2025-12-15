from django.urls import path
from .views import show_inventory

urlpatterns = [
    path('inventario/', show_inventory, name='inventario')
]
