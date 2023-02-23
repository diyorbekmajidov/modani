from django.contrib import admin
from .models import Catolog, Sub_category, Product
# Register your models here.
admin.site.register(Catolog)
admin.site.register(Sub_category)
admin.site.register(Product)