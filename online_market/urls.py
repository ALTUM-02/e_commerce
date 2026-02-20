from django .urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('product/<int:id>/', views.product_detail, name='product_detail'),
    path('add-product/', views.add_product, name='add_product'),
    path('add_to_cart/<int:id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('order_history/', views.order_history, name='order_history'),
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.user_dashboard, name='user_dashboard'),
    path('admin-dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('logout/', views.logout, name='logout'),
    
]