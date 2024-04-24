from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

from django import forms
from django.forms.widgets import TextInput, PasswordInput


class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1']


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())