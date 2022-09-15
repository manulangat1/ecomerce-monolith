from django.shortcuts import render
from rest_framework import generics, status
from rest_framework.response import Response 
from apps.products.models import Product, Category
from apps.products.serializers import ProductSerializer
# Create your views here.

class ProductListCreate(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    



