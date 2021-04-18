from django.shortcuts import render
from django.views import View

from .forms import ItemAddForm


# Create your views here.
class CreatePurchasingView(View):
    def get(self, request):
        return render(request, "purchasing_add.html", {'form': ItemAddForm()})
