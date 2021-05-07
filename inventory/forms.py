from django import forms
from .models import Item, Category

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Item

        fields = '__all__'

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['cat_id', 'option',]