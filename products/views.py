from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product

from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer


class list_products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
class product_detail(APIView):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,many=True,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)
    def put(self, request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    def patch(self,request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(instance=product,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk):
        product = Product.objects.get(pk=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)




