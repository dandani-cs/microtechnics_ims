from django.shortcuts import render
from django.views import View

from .forms import ItemAddFormset


# Create your views here.
class CreatePurchasingView(View):
    def get(self, request):
        return render(request,
                      "purchasing_add.html",
                      {'formset': ItemAddFormset()})

    # def post(self, request):
    #     formset = ItemAddFormset(request.POST)
    #     if formset.
