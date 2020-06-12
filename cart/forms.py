from django.forms import inlineformset_factory
from django import forms
from .models import CartLine, Cart
from django.utils.translation import gettext_lazy as _


PRODUCT_QUANTIY_CHOICES = [(i, str(i)) for i in range(1, 10)]




class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTIY_CHOICES,
                                      coerce=int,
                                      label=_('Quantity'))
    override = forms.BooleanField(required=False,
                                  initial=False,
                                  widget=forms.HiddenInput)

