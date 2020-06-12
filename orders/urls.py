from django.urls import path
from . import views
from django.utils.translation import gettext_lazy as _

app_name = 'orders'

urlpatterns = [
    path(_('checkout/'), views.order_create, name='order_create'),
]