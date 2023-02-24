from rest_framework import serializers
from .models import Product, Sub_category, Catolog

class CatologSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catolog
        fields = '__all__'

class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'