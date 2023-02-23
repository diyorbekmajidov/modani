from django.shortcuts import render
from .models import Catolog, Sub_category, product
from .serialzers import CatologSerializer, Sub_categorySerializer, ProductSerializer
from rest_framework import APIViev
from rest_framework.request import Request
from rest_framework.response import Response

# Create your views here.

class CatologListView(APIViev):
    def post(self, request:Request):
        data = request.data
        serializer = CatologSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self, request:Request):
        catologs = Catolog.objects.all()
        serializer = CatologSerializer(catologs, many=True)
        return Response(serializer.data)