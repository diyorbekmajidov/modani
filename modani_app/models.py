from django.db import models

# Create your models here.
class Catolog(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

class Sub_category(models.Model):
    name = models.CharField(max_length=200)
    catolog = models.ForeignKey(Catolog, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    dimensions = models.TextField()
    img = models.TextField()
    img_dimensions = models.TextField()
    features = models.TextField()
    sub_category = models.ForeignKey(Sub_category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name