from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from inventory.models import Item
from .forms import InventoryForm
from django.views import View

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
    template_name = "inventory/add_inv.html"
    add = InventoryForm()
    if request.method == 'POST':
        add = InventoryForm(request.POST, request.FILES)
        if add.is_valid():
            add.save()
            return redirect(template_name)
        else:
            return HttpResponseRedirect(reverse_lazy("home"))
    else:
        return render(request, template_name, {'add_form' : add})