from django.shortcuts import render
from django.views import View

# for redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse

# system info
from .forms import CustomUserCreationForm
from .models import User

# Create your views here.
class CreateUserView(View):
    template_name = "accounts_add.html"

    def get(self, request):
        return render(request, "accounts_add.html", {'form': CustomUserCreationForm()})

    def post(self, request, *args, **kwargs):
        user_form = CustomUserCreationForm(request.POST)

        if user_form.is_valid():
            user = user_form.save(commit = False)

            if user_form.cleaned_data['is_admin']:
                user.is_staff = True
                user.is_superuser = True

            user.save()

            return HttpResponseRedirect(reverse_lazy("home"))

        else:
            return render(request, "accounts_add.html", {'form': CustomUserCreationForm()})

def login(request):
    return render(request, 'accounts/login.html')

def forgotpass(request):
    return render(request, 'accounts/forgot_pass.html')

def home(request):
    return render(request, 'accounts/dashboard.html')
