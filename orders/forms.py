from django import forms
from .models import Order
from localflavor.us.forms import USZipCodeField


class OrderCreateForm(forms.ModelForm):
    postal_code = USZipCodeField()
    class Meta:
        model = Order
        fields = ['first_name', 'last_name',
                  'country', 'address',
                  'city', 'country_state',
                  'postal_code', 'phone',
                  'email']
