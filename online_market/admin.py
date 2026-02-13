from django.contrib import admin

from online_market.models import Product

# Register your models here.
admin.site.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'create_at')
    search_fields = ('name', 'description')