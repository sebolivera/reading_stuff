from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput

class LoginUpForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'loginusername', 'class':'form-control form-control-lg'}))
    password = forms.CharField(widget=PasswordInput(attrs={'id':'loginpassword', 'class':'form-control form-control-lg'}))
    class Meta:
      model = User
      fields =['username', 'password']