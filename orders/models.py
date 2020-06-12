from django.db import models
from shop.models import Product
from decimal import Decimal
from django.core.validators import MaxValueValidator, MinValueValidator
from coupons.models import Coupon
from django.utils.translation import gettext_lazy as _


class Order(models.Model):
    first_name = models.CharField(_('first name'),
                                  max_length=30)
    last_name = models.CharField(_('last name'),
                                 max_length=30)
    country = models.CharField(_('country'),
                               max_length=20)
    address = models.CharField(_('address'),
                               max_length=60)
    city = models.CharField(_('city'),
                            max_length=20)
    country_state = models.CharField(_('country/state'),
                                     max_length=20)
    postal_code = models.CharField(_('postal code'),
                                   max_length=10)
    phone = models.CharField(_('phone'),
                             max_length=9)
    email = models.EmailField(_('email'))
    paid = models.BooleanField(_('paid'),
                               default=False)
    braintree_id = models.CharField(max_length=150, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    coupon = models.ForeignKey(Coupon,
                               related_name='orders',
                               null=True,
                               blank=True,
                               on_delete=models.SET_NULL)
    discount = models.IntegerField(default=0,
                                   validators=[MinValueValidator(0),
                                               MaxValueValidator(100)])



    class Meta:
        ordering = ('-created',)


    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))

    def __str__(self):
        return f'Order {self.id}'


class OrderItem(models.Model):
    order = models.ForeignKey(Order,
                              related_name='items',
                              on_delete=models.CASCADE)
    product = models.ForeignKey(Product,
                                related_name='order_items',
                                on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

    def get_cost(self):
        return self.price * self.quantity



