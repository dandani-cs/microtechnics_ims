from django import forms
from django.forms import formset_factory

from inventory.models import Item

class ItemAddForm(forms.Form):
    all_items = Item.objects.order_by('name')

    item = forms.ChoiceField(choices=[(i.item_code, i.name) for i in all_items])
    quantity = forms.DecimalField()

ItemAddFormset = formset_factory(ItemAddForm, extra = 1)
