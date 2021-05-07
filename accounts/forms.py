from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name', 'is_admin', 'password1', 'password2')
      


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'last_name', 'first_name', 'is_admin')
        
