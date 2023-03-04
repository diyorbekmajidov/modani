from django.contrib import admin
from .models import Catolog, Sub_category, Product, Sale, Cart, Like
# Register your models here.
admin.site.register(Catolog)
admin.site.register(Sub_category)
admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(Cart)
admin.site.register(Like)