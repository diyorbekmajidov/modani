from rest_framework import serializers
from .models import Product, Sub_category, Catolog, Cart, Like, Sale

class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        fields = '__all__'

class CatologSerializer(serializers.ModelSerializer):
    sub_category = Sub_categorySerializer(many=True, read_only=True)

    class Meta:
        model = Catolog
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class SaleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sale
        fields = '__all__'