from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput, EmailInput
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'loginusername', 'class':'form-control form-control-lg'}))
    password = forms.CharField(widget=PasswordInput(attrs={'id':'loginpassword', 'class':'form-control form-control-lg'}))
    class Meta:
      model = User
      fields =['username', 'password']

class SignUpForm(UserCreationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'id_username', 'class':'form-control form-control-lg'}))
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=TextInput(attrs={'id':'id_first_name', 'class':'form-control form-control-lg'}))
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.', widget=TextInput(attrs={'id':'id_last_name', 'class':'form-control form-control-lg'}))
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.', widget=EmailInput(attrs={'id':'id_email', 'class':'form-control form-control-lg'}))
    password1 = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'id':'id_password1', 'class':'form-control form-control-lg'}))
    password2 = forms.CharField(label=_("Password confirmation"),
        widget=forms.PasswordInput(attrs={'id':'id_password2', 'class':'form-control form-control-lg'}),
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )