from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'accounts/login.html')

def forgotpass(request):
    return render(request, 'accounts/forgot_pass.html')

def home(request):
    return render(request, 'dashboard.html')