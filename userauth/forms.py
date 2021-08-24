from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'loginusername', 'class':'form-control form-control-lg'}))
    password = forms.CharField(widget=PasswordInput(attrs={'id':'loginpassword', 'class':'form-control form-control-lg'}))
    class Meta:
      model = User
      fields =['username', 'password']

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )