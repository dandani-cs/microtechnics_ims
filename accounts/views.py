from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html')

def forgotpass(request):
    return render(request, 'forgot_pass.html')

def newpass(request):
    return render(request, 'add_new_pass.html')

def home(request):
    return render(request, 'dashboard.html')