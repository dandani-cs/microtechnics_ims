from django import forms
from django.forms import formset_factory
from django.db.models import Q

from inventory.models import Item
from orders.models import Order

class OrderConfirmForm(forms.ModelForm):
    class Meta:
        all_users = Item.objects.all()
        model     = Order
        fields    = ( 'requested_user', ) # Not necessarily an employee
