from django.http.response import HttpResponseBadRequest
from .models import Post

def has_publications(author):
    if author.is_authenticated: # am I allowed to do this ?
        post_list = Post.objects.all().filter(author=author)
        if post_list.count() > 0:
            return True
    return False

def require_AJAX(function):
    def wrap(request, *args, **kwargs):
        if not request.is_ajax():
            return HttpResponseBadRequest()
        return function(request, *args, **kwargs)

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

def set_text_color(bg_color):
    if bg_color and bg_color == "dark":
        return "light"
    else:
        return "dark"