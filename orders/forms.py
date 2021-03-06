from django import forms
from django.forms import formset_factory
from django.db.models import Q

from inventory.models import Item
from orders.models import Order

class OrderConfirmForm(forms.ModelForm):
    class Meta:
        model     = Order
        fields    = ( 'requested_user', ) # Not necessarily an employee
        widgets   = { 'requested_user' : forms.Select(attrs = { 'class' : 'form-control' }) }
