from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Proveedor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank='N/A')
    number_phone = models.CharField(max_length=20)
    address = models.TextField()
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.name 

class Product_Provedor(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    proveedor = models.ForeignKey(Proveedor, on_delete= models.CASCADE)
    
    def __str__(self):
        return self.pk
    
class Operation(models.Model):
    operation_type = models.BooleanField()
    total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    money_devolution = models.BooleanField(null=True, blank=True)
    product_replacement = models.BooleanField(null=True, blank=True)
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.pk


