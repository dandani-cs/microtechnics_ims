from django import forms

from inventory.models import Item

class ItemAddForm(forms.Form):
    all_items = Item.objects.order_by('name')

    item = forms.ChoiceField(choices=[(i.item_code, i.name) for i in all_items])
    quantity = forms.DecimalField()
