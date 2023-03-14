from django.db import models

# Create your models here.
class Catolog(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Sub_category(models.Model):
    names = models.CharField(max_length=200)
    catolog = models.ForeignKey(Catolog, on_delete=models.CASCADE, related_name='sub_category')
    
    def __str__(self):
        return self.names

class Product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    description = models.TextField(max_length=500)
    dimensions = models.TextField(max_length=500)
    img = models.TextField(max_length=500)
    img_dimensions = models.TextField(max_length=500)
    features = models.TextField(max_length=500)
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.product_name
    
class Sale(models.Model):
    percent = models.IntegerField()
    product = models.ManyToManyField(Product) 
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return 'Sale'
    
class Cart(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return 'Cart'

class Like(models.Model):
    product = models.ManyToManyField(Product)
    comment = models.TextField(max_length=50)
    def __str__(self):
        return 'Like'