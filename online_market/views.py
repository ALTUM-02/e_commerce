from django.shortcuts import render,redirect
from .models import Product
from django.contrib.auth import login, logout, authenticate
from .forms import RegisterForm,LoginForm

# Create your views here.
def home(request):
    product = Product.objects.all()
    return render(request, 'online_market/home.html', {'products': product})

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
    return render(request, 'online_market/register.html', {'form': form})

def login(request):
    form = LoginForm()
    if request.method == 'POST':
        Form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()
            register(request, user)
            return redirect('home')
    return render(request, 'online_market/login.html', {'form':form})  

def logout_user(request):
    logout(request)
    return redirect('login')  
        