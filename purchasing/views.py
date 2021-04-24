from django.shortcuts import render
from django.views import View
from django.db.models import Q
from decimal import *

from .forms import ItemAddForm, ItemFormSet, PurchaseConfirmForm
from .models import Purchasing

from inventory.models import Item

# Create your views here.
class ConfirmPurchasingView(View):
    def get(self, request):
        #TODO: retrieve from session data
        purchased    = { 'cc85cbafb5' : 10 , '6737aa7594' : 20 }
        item_details = Item.objects.filter(item_code__in = purchased.keys())

        for item in item_details:
            item.quantity = purchased[item.item_code]

        subtotal     = sum([ item.price * purchased[item.item_code] for item in item_details])
        autofilled_data = {
                'total_price'   : subtotal,
                'items'         : purchased
            }

        purchase_form = PurchaseConfirmForm(initial = autofilled_data)

        return render(request, "purchasing_confirm.html", { 
                        'form'    : purchase_form,
                        'item_set': item_details
                    })

class CreatePurchasingView(View):
    def post(self, request):
        item_formset = ItemFormSet(request.POST)
        
        if item_formset.is_valid():
            for form in item_formset:
                data = form.cleaned_data
                print(data)
        return HttpResponseRedirect(reverse_lazy("purchasing_confirm"))

    def get(self, request):
        item_formset = ItemFormSet()
        return render(request, "purchasing_add.html", {'form': item_formset})
