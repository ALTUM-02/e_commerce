from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Product

class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
class LoginForm(forms.Form):
    username = forms.CharField(min_length=100)
    password = forms.CharField(widget=forms.PasswordInput)
    
class ProductForm(forms.modelForm):
    class Meta:  
        