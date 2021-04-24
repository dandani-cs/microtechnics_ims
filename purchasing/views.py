from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q
from decimal import *

from .forms import ItemAddForm, ItemFormSet, PurchaseConfirmForm
from .models import Purchasing, StatusPurchasingOptions

from inventory.models import Item
from accounts.models import User

import json

# Create your views here.
class ConfirmPurchasingView(View):
    def post(self, request):
        purchase_form       = PurchaseConfirmForm(request.POST)
        final_purchase_info = (request.session['final_purchase_info'] if 'final_purchase_info' in request.session else None)
        current_user        = get_user(request.user)

        if purchase_form.is_valid():
            purchase             = purchase_form.save(commit = False)
            purchase.items       = final_purchase_info['items']
            purchase.total_price = Decimal(final_purchase_info['subtotal'])

            if current_user != None and current_user.is_admin:
                print("User making the purchase is an admin")
                purchase.status         = StatusPurchasingOptions.STATUS_APPROVED
                purchase.approved_admin = current_user

            item_set = Item.objects.filter(Q(item_code__in = purchase.items.keys()))
            for item in item_set:
                item.quantity     = item.quantity + purchase.items[item.item_code]
                item.max_quantity = max(item.quantity, item.max_quantity)
                item.save()

            purchase.save()

        return render(request, "purchasing_confirm.html")

    def get(self, request):
        items_info      = (request.session['purchasing_info'] if 'purchasing_info' in request.session else None)
        purchased_items = { item[0] : item[1] for item in items_info } # To be stored in JSON field

        item_set = Item.objects.filter(Q(item_code__in = purchased_items.keys()))
        for item in item_set:
            item.quantity = purchased_items[item.item_code]

        subtotal     = sum([ item.price * item.quantity for item in item_set ])
        current_user = get_user(request.user)

        request.session['final_purchase_info'] = { 'items'    : purchased_items, 
                                                   'subtotal' : round(float(subtotal), 2) }

        return render(request, "purchasing_confirm.html", 
                                    { 
                                        'item_set'      : item_set,
                                        'subtotal'      : subtotal,
                                        'purchase_form' : PurchaseConfirmForm(),
                                        'current_user'  : current_user
                                    })

class CreatePurchasingView(View):
    def post(self, request):
        items = [[i.item_code, i.name] for i in Item.objects.all()]
        item_formset = ItemFormSet(request.POST)

        if item_formset.is_valid():
            request.session['purchasing_info'] = [(form.cleaned_data['item'], form.cleaned_data['quantity']) for form in item_formset]
        return HttpResponseRedirect(reverse_lazy('purchasing_confirm')) 

    def get(self, request):
        items = [[i.item_code, i.name] for i in Item.objects.all()]
        item_formset = ItemFormSet()
        return render(request, "purchasing_add.html", {'form': item_formset, 'item_codes': json.dumps(items)})


def get_user(user):
    try:
        return User.objects.get(username = user)
    except User.DoesNotExist:
        return None
