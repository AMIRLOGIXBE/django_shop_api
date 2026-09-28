from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from products.models import Product

from django.shortcuts import render
from .models import Product
from .serializer import ProductSerializer


#
# def products(request):
#     products = Product.objects.filter(is_active=True).all()
#     return render(request, 'shop.html', {'products': products})
# def product_detail(request,pk):
#     product=Product.objects.get(pk=pk)
#     return render(request,'product-details.html',{'product':product})

class list_products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)
class product_detail(APIView):
    def get(self, request,pk):
        product = Product.objects.get(pk=pk)
        serializer = ProductSerializer(product,context={"request":request})
        return Response(serializer.data,status=status.HTTP_200_OK)