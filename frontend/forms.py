from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from .models import *

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email','password1','password2')
        widgets = {
            'first_name': forms.TextInput,
            'Last_name': forms.TextInput,
            'username': forms.TextInput,
            'email': forms.EmailInput,
            'password1': forms.PasswordInput,
            'password2': forms.PasswordInput,
        }

        