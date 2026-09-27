from django.shortcuts import render
from products.models import Product

from django.shortcuts import render
from .models import Product


def products(request):
    products = Product.objects.filter(is_active=True).all()
    return render(request, 'shop.html', {'products': products})
def product_detail(request,pk):
    product=Product.objects.get(pk=pk)
    return render(request,'product-details.html',{'product':product})