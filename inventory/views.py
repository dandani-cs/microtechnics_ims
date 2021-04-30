from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from inventory.models import Item
from .forms import InventoryForm
from django.views import View
from .filters import ItemFilter

# Create your views here.
class ItemListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'
    model         = Item
    template_name = "inventory/item_view.html"

class ItemEditListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'
    model = Item
    template_name = "inventory/edit_inv.html"

def addItem(request):
    add = InventoryForm()
    if request.method == 'POST':
        add = InventoryForm(request.POST)
        if add.is_valid():
            add.save()
            return redirect('view_items')

    context = {'add_form': add}
    return render(request, 'inventory/add_inv.html', context)

def editItem(request):
    update = InventoryForm()
    context = {'update_form': update}
    return render(request, 'inventory/add_inv.html', context)