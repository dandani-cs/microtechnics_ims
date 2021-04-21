from django.shortcuts import render
from django.views import View

from .forms import ItemAddForm, ItemFormSet
from inventory.models import Item

import json

# Create your views here.
class CreatePurchasingView(View):
    def post(self, request):
        items = [i.item_code for i in Item.objects.all()]
        item_formset = ItemFormSet(request.POST)

        if item_formset.is_valid():
            print([(form.cleaned_data['item'], form.cleaned_data['quantity']) for form in item_formset])

        return render(request, "purchasing_add.html", {'form': ItemFormSet(), 'item_codes': json.dumps(items)})

    def get(self, request):
        item_formset = ItemFormSet()
        return render(request, "purchasing_add.html", {'form': item_formset})
