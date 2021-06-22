from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"


class PostDetail(TemplateView):
    template_name = "post/post.html"