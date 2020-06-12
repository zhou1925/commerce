from django import template
from ..models import Product


register = template.Library()

@register.simple_tag
def show_latest_products(count=3):
    return Product.objects.order_by('-created')[:count]

@register.simple_tag
def show_latest_products2(count=6):
    return Product.objects.order_by('-created')[3:count]