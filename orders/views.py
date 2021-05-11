from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.db.models import Q

from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

import json
from decimal import *

from inventory.models import Item
from purchasing.forms import ItemFormSet
from accounts.models import User

from .forms import OrderConfirmForm
from .models import Order

# Create your views here.
class ConfirmOrderView(View):
    def post(self, request):
        order_form       = OrderConfirmForm(request.POST)
        final_order_info = (request.session['final_order_info'] if 'final_order_info' in request.session else None)
        current_user     = get_user(request.user)

        if order_form.is_valid():
            order             = order_form.save(commit = False)
            order.items       = final_order_info['items']
            order.total_price = Decimal(final_order_info['subtotal'])

            if current_user != None and current_user.is_admin:
                order.is_approved    = True
                order.approved_admin = current_user

            order.save()

        return render(request, "order_confirm.html")

    def get(self, request):
        items_info    = (request.session['order_info'] if 'order_info' in request.session else None)
        ordered_items = { item[0] : item[1] for item in items_info }

        item_set = Item.objects.filter(Q(item_code__in = ordered_items.keys()))
        for item in item_set:
            item.quantity = ordered_items[item.item_code]

        subtotal     = sum([ item.price * item.quantity for item in item_set ])
        current_user = get_user(request.user)

        print("Subtotal", subtotal)

        request.session['final_order_info'] = { 'items'    : ordered_items, 
                                                'subtotal' : round(float(subtotal), 2) }


        return render(request, "order_confirm.html", 
                                            {
                                                'item_set'    : item_set,
                                                'subtotal'    : subtotal,
                                                'order_form'  : OrderConfirmForm,
                                                'current_user': current_user
                                            })

class CreateOrderView(View):
    def post(self, request):
        # TODO: Only include items whose quantity > 0
        items = [[i.item_code, i.name] for i in Item.objects.all()]
        item_formset = ItemFormSet(request.POST)

        if item_formset.is_valid():
            request.session['order_info'] = [(form.cleaned_data['item'], form.cleaned_data['quantity']) for form in item_formset]

        return HttpResponseRedirect(reverse_lazy('order_confirm')) 

    def get(self, request):
        items = [[i.item_code, i.name, i.quantity ] for i in Item.objects.all()]
        item_formset = ItemFormSet()
        return render(request, "order_add.html", { 'form':       item_formset, 
                                                   'item_codes': json.dumps(items) })

class OrderListView(LoginRequiredMixin, ListView):
    login_url           = 'final_login'
    redirect_field_name = 'redirect_to'

    model         = Order
    template_name = 'order_view.html'

class OrderDetailView(LoginRequiredMixin, DetailView):
    login_url           = 'final_login'
    redirect_field_name = 'redirect_to'
    model         = Order
    template_name = 'order_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['order_items'] = context['object'].items

        context['order_item_details'] = dict()

        keys = list(context['object'].items.keys())

        for item_key in keys:
            item = Item.objects.get(item_code=item_key)
            item.quantity = context['object'].items[item_key]
            context['order_item_details'][item_key] = item

        return context

class OrderUpdateStatusView(View):
    def post(self, request, order_num):
        order = get_order(order_num)

        if 'btn_approve' in request.POST:
            order.is_approved    = True
            order.approved_admin = request.user

            item_set = Item.objects.filter(item_code__in = order.items.keys())
            for item in item_set:
                item.quantity = item.quantity - order.items[item.item_code]
                item.save()

        order.save()

        return HttpResponseRedirect(reverse_lazy('order_detail', args = [order_num]))

class OrderCancelConfirmView(LoginRequiredMixin, View):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'

    def get(self, request, order_num):
        order = get_order(order_num)
        return render(request, 'order_cancel_confirm.html', {"order": order, "total_items": len(order.items)})


    def post(self, request, order_num):
        order = get_order(order_num)
        print("Cancelled order#", order.order_num)
        return HttpResponseRedirect(reverse_lazy('order_detail', args=[order_num]))


def get_order(order_no):
    try:
        return Order.objects.get(order_num = order_no)
    except Order.DoesNotExist:
        return None

def get_user(user):
    try:
        return User.objects.get(username = user)
    except User.DoesNotExist:
        return None
