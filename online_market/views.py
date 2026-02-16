from django.shortcuts import render,redirect
from .models import Product,Cart, CartItem,Order
from django.contrib.auth import authenticate,  login as auth_login, logout
from .forms import RegisterForm,LoginForm,ProductForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def home(request):
    products = Product.objects.all()
    return render(request, 'online_market/home.html', {'products': products})

def product_detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'online_market/product_detail.html', {'product': product})

def add_product(request):
    if request.method == "POST":
        name = request.POST.get('name')
        price = request.POST.get('price')
        image = request.POST.get('image')
        description = request.POST.get('description')
        stock = request.POST.get('stock')
        
      #  Product.objects.create(
       #     name=name,
        #    price=price,
         #   image=image,
          #  description=description,
           # stock=stock,
            #User=request.user
        #)
        
        return redirect('home')
    
    return render(request, 'online_market/add_product.html')      
        


def add_to_cart(request, id):
    product = Product.objects.get(id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    
    if not created:
        cart_item.quantity += 1
        
    else:
        cart_item.quantity = 1   
         
    cart_item.save()
    
    return redirect('cart')  


def cart_view(request):
    cart, created = Cart.objects.get_or_create(user=request.user)  
    items = CartItem.objects.filter(cart=cart)
    return render(request, 'online_market/cart.html', {'items': items})

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    return render(request, 'online_market/register.html', {'form': form})

def login_view(request):
    #form = LoginForm()
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            auth_login(request, user)
            
            if user.is_superuser:
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
            
    return render(request, 'online_market/login.html')        
        #Form = LoginForm(request.POST)
        #if form.is_valid():
          #  user = form.save()
           # register(request, user)
            #return redirect('home')
    #return render(request, 'online_market/login.html', {'form':form})  
    
def user_dashboard(request):
    return render(request, 'online_market/user_dashboard.html')    

def admin_dashboard(request):
    data = {
        'orders': Order.objects.count(),
        'products': Product.objects.count()
    }
    return render(request, 'online_market/user_dashboard.html')

def logout_view(request):
    logout(request)
    return redirect('login')  

def order_history(request):
    user_order = Order.objects.filter(user=request.user).order_by('created_at')
    context = {'order': user_order}
    return render(request, 'order_history.html', context)

    
        