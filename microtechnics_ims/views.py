from django.shortcuts import render
from accounts.models import User
from django.http import HttpResponse
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
# import csv
import csv

# date time
import datetime

class UserLoginView(View):
    def post(self, request, *args,**kwargs):
        email = request.POST['email']
        password = request.POST['password']
        username = get_user(email)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse_lazy('home'))

        else:
         
            return render(request, 'login/login.html', {'error': True})

    def get(self, request):
        return render(request, 'login/login.html', {'error':False})

def get_user(email):
    try: 
        return User.objects.get(email=email.lower())
    except User.DoesNotExist:
        return None

def home(request):
    users = User.objects.all()
    return render(request, 'dashboard.html', {'users': users})

def export_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition']='attachment; filename=accounts.csv'

    writer = csv.writer(response)
    writer.writerow(['First Name', 'Last Name'])
    users = User.objects.filter(username=request.user)

    for user in users:
        writer.writerow([user.first_name, user.last_name])

    return response
