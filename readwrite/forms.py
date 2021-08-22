from .models import Comment, Post, User
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import TextInput, PasswordInput

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':3, 'cols':50}),
        }

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content')

class LoginUpForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'id':'loginusername', 'class':'form-control form-control-lg'}))
    password = forms.CharField(widget=PasswordInput(attrs={'id':'loginpassword', 'class':'form-control form-control-lg'}))
    class Meta:
      model = User
      fields =['username', 'password']