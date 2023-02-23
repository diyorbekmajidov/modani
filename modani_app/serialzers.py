from rest_framework import serializers
from .models import Product, Sub_category, Catolog

class CatologSerializer(serializers.ModelSerializer):
    class Meta:
        model = Catolog
        fields = '__all__'

class Sub_categorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_category
        name = serializers.PrimaryKeyRelatedField(queryset=Catolog.objects.all())
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        name = serializers.PrimaryKeyRelatedField(queryset=Sub_category.objects.all())
        fields = '__all__'