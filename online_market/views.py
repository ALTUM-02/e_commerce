from django.shortcuts import render,redirect
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'online_market/home.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'online_market_detail.html', {'product': product})