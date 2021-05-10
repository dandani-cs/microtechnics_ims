from django.shortcuts import render, redirect
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from inventory.models import Item, Category
from .forms import InventoryForm, CategoryForm
from django.views import View
from .filters import ItemFilter
from bootstrap_modal_forms.generic import (
    BSModalReadView
)

# Create your views here.
class ItemListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'
    model         = Item
    template_name = "inventory/item_view.html"
    item_Filter = ItemFilter()
    paginate_by = 10

class ItemReadView(BSModalReadView):
    model = Item
    template_name = 'inventory/read_item.html'

def addItem(request):
    add = InventoryForm()
    if request.method == 'POST':
        add = InventoryForm(request.POST)
        if add.is_valid():
            add.save()
            return redirect('view_items')

    context = {'form': add}
    return render(request, 'inventory/add_inv.html', context)

def editItem(request, pk):
    #update = InventoryForm()
    #context = {'update_form': update}
    template_name = 'inventory/edit_inv.html'
    #item_edit = Item.objects.get(pk=pk)
    #update = InventoryForm()
    
    #if request.method == 'POST':
    #    update = InventoryForm(request.POST)
    #    if update.is_valid():
    #        update.save()
    #        return redirect('view_items')

    #context = {'edit_form': update}
    pk = str(pk)

    try:
        select_item = Item.objects.get(item_code = pk)
    except Item.DoesNotExist:
        return redirect('view_items')
    update_form = InventoryForm(request.POST or None, instance = select_item)
    if update_form.is_valid():
        update_form.save()
        print("sucessfully updated")
        return redirect('view_items')
    return render(request, template_name, {'form': update_form})

def deleteItem(request, pk):
    item = Item.objects.get(pk=pk)

    try:
        if request.method == 'POST':
            item.delete()
            return redirect('view_items')
    except item.DoesNotExist:
        print("Item does not exist")
        return redirect('view_items')

    context = {'item': item}
    return render(request, 'inventory/delete_item.html', context)

## categories

class CategoryListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    template_name = 'inventory/category_view.html'
    redirect_field_name = 'redirect_to'
    model = Category
    paginate_by = 10

class CategoryReadView(BSModalReadView):
    model = Category
    template_name = 'inventory/read_category.html'

def addCategory(request):
    addCat = CategoryForm()
    if request.method == 'POST':
        addCat = CategoryForm(request.POST)
        if addCat.is_valid():
            addCat.save()
            return redirect('view_category')

    context = {'form': addCat}
    return render(request, 'inventory/add_category.html', context)

def editCategory(request, pk):
    #update = InventoryForm()
    #context = {'update_form': update}
    template_name = 'inventory/edit_category.html'
    #item_edit = Item.objects.get(pk=pk)
    #update = InventoryForm()
    
    #if request.method == 'POST':
    #    update = InventoryForm(request.POST)
    #    if update.is_valid():
    #        update.save()
    #        return redirect('view_items')

    #context = {'edit_form': update}
    pk = str(pk)

    try:
        select_cat = Category.objects.get(cat_id = pk)
    except Category.DoesNotExist:
        return redirect('view_category')
    update_form = CategoryForm(request.POST or None, instance = select_cat)
    if update_form.is_valid():
        update_form.save()
        print("sucessfully updated")
        return redirect('view_category')
    return render(request, template_name, {'form': update_form})

def deleteCategory(request, pk):
    category = Category.objects.get(pk=pk)

    try:
        if request.method == 'POST':
            category.delete()
            return redirect('view_category')
    except Category.DoesNotExist:
        print("Category does not exist")
        return redirect('view_category')

    context = {'cat': category}
    return render(request, 'inventory/delete_category.html', context)