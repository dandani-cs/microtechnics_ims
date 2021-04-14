from django.shortcuts import render
from django.views.generic.list import ListView
from inventory.models import Item

# Create your views here.
class ItemListView(ListView):
    model         = Item
    template_name = "inventory/item_view.html"
