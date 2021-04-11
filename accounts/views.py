from django.shortcuts import render
from django.views import View

from .forms import CustomUserCreationForm

# Create your views here.
class CreateUserView(View):
    template_name = "accounts_add.html"

    def get(self, request):
        return render(request, "accounts_add.html", {'form': CustomUserCreationForm()})
