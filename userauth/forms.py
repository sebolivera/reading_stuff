from .models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import ClearableFileInput, EmailInput, PasswordInput, TextInput
from django.utils.translation import ugettext, ugettext_lazy as _

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'id_username', 'class':'form-control form-control-lg', 'autofocus':False}))
    password = forms.CharField(label=_("Password"),
        widget=forms.PasswordInput(attrs={'id':'id_password1', 'class':'form-control form-control-lg'}))
    class Meta:
      model = User
      fields =['username', 'password']

class SignUpForm(UserCreationForm):
    username = forms.CharField(required=True, widget=TextInput(attrs={'id':'id_username', 'class':'form-control form-control-lg', 'autofocus':False}))
    pen_name = forms.CharField(max_length=30, required=False, help_text='Optionnal. Can be different than your username.', widget=TextInput(attrs={'id':'id_pen_name', 'class':'form-control form-control-lg'}))
    profile_picture = forms.ImageField(required=False, help_text='Optional.', widget=ClearableFileInput(attrs={'id':'id_profile_pic', 'class':'form-control form-control-lg'}))
    email = forms.EmailField(max_length=254, required=True, help_text='Required. Inform a valid email address.', widget=EmailInput(attrs={'id':'id_email', 'class':'form-control form-control-lg'}))
    password1 = forms.CharField(label=_("Password"), required=True,
        widget=forms.PasswordInput(attrs={'id':'id_password1', 'class':'form-control form-control-lg'}))
    password2 = forms.CharField(label=_("Password confirmation"), required=True,
        widget=forms.PasswordInput(attrs={'id':'id_password2', 'class':'form-control form-control-lg'}),
        help_text=_("Enter the same password as above, for verification."))

    class Meta:
        model = User
        fields = ('pen_name', 'profile_picture', 'username', 'email', 'password1', 'password2', )