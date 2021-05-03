from django.shortcuts import render, redirect
from django.views import View
from django.views.generic.list import ListView
# for redirect
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.http import HttpResponse

# system info
from .forms import CustomUserCreationForm, CustomUserChangeForm
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

            return HttpResponseRedirect(reverse_lazy("show_list"))

        else:
            print(user_form.errors)
            return render(request, "accounts_add.html", {'form': CustomUserCreationForm()})


  

def forgotpass(request):
    return render(request, 'forgot_pass.html')

def newpass(request):
    return render(request, 'add_new_pass.html')

def editUser(request, employee_id):
    emp = User.objects.get(username = employee_id)   
    return render(request, "edit_account.html", {'emp': emp})

def updateUser(request, employee_id):
    emp = User.objects.get(username = employee_id)  
    form = CustomUserCreationForm(request.POST, instance = emp)  
    if form.is_valid():  
        emp = form.save(commit = False)

        emp.save()  
    return redirect("show_list")    
   

def deleteUser(request, employee_id):
    emp = User.objects.get(username= employee_id)  
    emp.is_active = False
    emp.save()
    return redirect("show_list")

def userProfile(request, employee_id):
    emp = User.objects.get(username = employee_id)
    return render(request, "user_profile.html", {'emp': emp})

class usermanagement(ListView):
    model = User
    template_name = "UserMngmtAdmin.html"