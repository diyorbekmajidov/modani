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
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=1)
    description = models.TextField()
    dimensions = models.TextField()
    img = models.TextField()
    img_dimensions = models.TextField()
    features = models.TextField()
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Sale(models.Model):
    percent = models.IntegerField()
    product = models.ManyToManyField(Product) 
    start = models.DateTimeField()
    end = models.DateTimeField()

    def __str__(self):
        return self.sale
    
class Cart(models.Model):
    product = models.ManyToManyField(Product)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return self.user

class Like(models.Model):
    product = models.ManyToManyField(Product)
    comment = models.TextField()
    def __str__(self):
        return self.user