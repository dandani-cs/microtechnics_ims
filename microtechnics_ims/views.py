from django.shortcuts import render
from accounts.models import User
from django.http import HttpResponse

# import csv
import csv

# date time
import datetime

def login(request):
    return render(request, 'login.html')

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
