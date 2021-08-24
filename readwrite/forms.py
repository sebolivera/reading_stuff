from .models import Comment, TextPost
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
        widgets = {
          'body': forms.Textarea(attrs={'rows':3, 'cols':50}),
        }

class TextPostForm(forms.ModelForm):
    class Meta:
        model = TextPost
        fields = ('title', 'content')
