from django import forms

from inventory.models import Items

class ItemAddForm(forms.Form):
    all_items = Items.objects.order_by('name')

    item = forms.ChoiceField(choices=[i.name for i in all_items])
    quantity = forms.DecimalField()
