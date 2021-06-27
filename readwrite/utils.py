from .models import Post

def has_publications(author):
    if author.is_authenticated: # am I allowed to do this ?
        post_list = Post.objects.all().filter(author=author)
        if post_list.count() > 0:
            return True
    return False