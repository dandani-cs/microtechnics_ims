from django import forms
from .models import Item

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = [
            "item_code",
            "name",
            "price",
            "quantity",
            "category",
            "max_quantity",
            "description",
        ]