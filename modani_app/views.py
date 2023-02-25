from django.shortcuts import render
from .models import Catolog, Sub_category, Product
from .serialzers import CatologSerializer, Sub_categorySerializer, ProductSerializer
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.

class CatologListView(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = CatologSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Getcatolog(APIView):
    def get(self, request:Request):
        catologs = Catolog.objects.all()
        serializer = CatologSerializer(catologs, many=True)
        return Response(serializer.data)

class SubcategoryListView(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = Sub_categorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Subcategoryget(APIView):        
    def get(self, request:Request,id):
        name = Catolog.objects.get(id=id)
        sub_categories = Sub_category.objects.filter(catolog=name)
        serializer1 = CatologSerializer(name, many=False)
        serializer = Sub_categorySerializer(sub_categories, many=True)
        data = {
            'catolog': serializer1.data,
            'sub_categories': serializer.data
        }
        return Response(data)

class ProductListView(APIView):
    def post(self, request:Request):
        data = request.data
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class Productget(APIView):
    def get(self, request:Request,id):
        name = Sub_category.objects.get(id=id)
        products = Product.objects.filter(sub_category=name)
        serializer1 = Sub_categorySerializer(name, many=False)
        serializer = ProductSerializer(products, many=True)
        data = {
            'sub_category': serializer1.data,
            'products': serializer.data
        }
        return Response(data)
        