from django.contrib import admin
from .models import Product, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class Product(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'available', 'quantity', 'created']
    list_filter = ['price', 'available']
    list_editable = ['price', 'available', 'quantity']
    prepopulated_fields = {'slug': ('name',)}

