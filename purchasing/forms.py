from django import forms
from django.forms import formset_factory
from django.db.models import Q

from inventory.models import Item
from .models import Purchasing

class PurchaseConfirmForm(forms.ModelForm):
    class Meta:
        all_users = Item.objects.all()
        model     = Purchasing
        fields    = ( 'requested_user', ) # Not necessarily an employee

class ItemAddForm(forms.Form):
    all_items = Item.objects.order_by('name')

    item     = forms.ChoiceField(choices=[(i.item_code, i.name) for i in all_items])
    quantity = forms.IntegerField()
    quantity.widget.attrs.update({ 'class': 'item-qty form-control'})
    item.widget.attrs.update({ 'class'   : 'form-control form-select',
                               'onchange': 'update_item_choices()'})

ItemFormSet = formset_factory(ItemAddForm, extra = 1)
