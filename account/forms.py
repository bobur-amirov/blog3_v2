from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import Account


class RegisterForm(UserCreationForm):
    class Meta:
        model = Account
        fields = ['username', 'email', 'phone_number', 'password1', 'password2']

        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username kiriting'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email kiriting'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone number kiriting'}),
        }
