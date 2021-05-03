from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import ItemAddForm, ItemFormSet
from .models import Purchasing
from inventory.models import Item

import json

# Create your views here.
class CreatePurchasingView(View):
    def post(self, request):
        items = [[i.item_code, i.name] for i in Item.objects.all()]
        item_formset = ItemFormSet(request.POST)

        if item_formset.is_valid():
            request.session['purchasing_info'] = [(form.cleaned_data['item'], form.cleaned_data['quantity']) for form in item_formset]

        return render(request, "purchasing_add.html", {'form': ItemFormSet(), 'item_codes': json.dumps(items)})

    def get(self, request):
        items = [[i.item_code, i.name] for i in Item.objects.all()]
        item_formset = ItemFormSet()
        return render(request, "purchasing_add.html", {'form': item_formset, 'item_codes': json.dumps(items)})


class PurchasingListView(LoginRequiredMixin, ListView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'

    model = Purchasing
    template_name = "purchasing_view.html"


class PurchasingDetailView(LoginRequiredMixin, DetailView):
    login_url = 'final_login'
    redirect_field_name = 'redirect_to'

    model = Purchasing
    template_name = "purchasing_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['items'] = json.loads['items']

        return context
