from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'online_market/home.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'online_market_detail.html', {'product': product})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'online_market/reister.html', {'form': form})


                    