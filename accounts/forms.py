from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import User

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        models = User
        fields = (email, last_name, first_name, is_admin)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        models = User
        fields = (email, last_name, first_name, is_admin)

        
