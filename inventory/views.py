from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from inventory.models import Item

# Create your views here.
class ItemListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'

    model         = Item
    template_name = "inventory/item_view.html"
