from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name',
                    'country', 'address', 'postal_code',
                    'city', 'paid']
    list_filter = ['paid', 'created', 'updated']
    list_editable = ['paid',]
    inlines = [OrderItemInline]
