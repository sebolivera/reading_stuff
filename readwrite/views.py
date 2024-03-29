from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import TextPost, Post, Comment, Book, Chapter
from userauth.models import User
from .forms import CommentForm, TextPostForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import slugify
from django.http import HttpResponseBadRequest
from django.template.loader import render_to_string
from django.db.models import Q
from .utils import has_publications, require_AJAX
from readwrite.utils import set_text_color
from django.utils.translation import gettext as _
# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    context = {}

    def get(self, request):
        self.context['post_list'] = Post.objects.all().filter(status=1)
        self.context['has_publications'] = has_publications(self.request.user)
        response = render(request, self.template_name, self.context)
        if request.user.is_authenticated :
            self.context['favorites'] = request.user.favorites.all()
            this_user = User.objects.get(pk=request.user.pk)
            response.set_cookie('site_color_mode', this_user.color_mode, max_age = 5000000)
            response.set_cookie('site_text_color_mode', set_text_color(this_user.color_mode), max_age=5000000) #arguably a stupidly convoluted way to do it, but I really hate jinja
        elif request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
            response.set_cookie('site_color_mode', request.COOKIES.get('site_color_mode'), max_age = 5000000)
            response.set_cookie('site_text_color_mode', set_text_color(request.COOKIES.get('site_color_mode')), max_age=5000000)
        else:
            response.set_cookie('site_color_mode', 'light', max_age = 5000000)
            response.set_cookie('site_text_color_mode', 'dark', max_age=5000000)
        
        return response

class PublicationView(TemplateView):
    template_name = "publications.html"
    context = {}

    def get(self, request):
        post_list = Post.objects.all().filter(author=self.request.user)
        self.context['post_list'] = post_list
        self.context['has_publications'] = has_publications(self.request.user)
        response=render(request, self.template_name, self.context)
        if request.user.is_authenticated :
            self.context['favorites'] = request.user.favorites.all()
            response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
            response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
        elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
            response.set_cookie('site_color_mode', 'light', max_age = 5000000)
            response.set_cookie('site_text_color_mode', 'dark', max_age = 5000000)
        return response

class FavoritedView(TemplateView):
    template_name = "favorites.html"
    context = {}

    def get(self, request):
        self.context['fav_view'] = True
        self.context['post_list'] = self.request.user.favorites.all()
        self.context['has_publications'] = has_publications(self.request.user)
        response = render(request, self.template_name, self.context)
        if self.request.user.is_authenticated :
            self.context['favorites'] = request.user.favorites.all()
            response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
            response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
        elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
            response.set_cookie('site_color_mode', 'light', max_age = 5000000)
            response.set_cookie('site_text_color_mode', 'dark', max_age = 5000000)
        return response

    

def postDetail(request, slug): # not a class bc post & get annoying
    template_name = "post/post.html"
    the_post = get_object_or_404(Post, slug=slug)
    comments = the_post.comments.filter(active=True)
    context = {'post' : the_post, 'comments' : comments}
    new_comment = None

    if request.method == 'POST' and request.user.is_authenticated:
        context = {'post' : the_post}
        context['favorites'] = request.user.favorites.all()
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # doesn't add it to the db as we need to link the post
            new_comment.author = request.user
            if request.user.has_perm('moderate'):
                new_comment.active = True
                message_to_pass = 'Your comment has successfully been posted!'
            else:
                message_to_pass = 'Your comment has been submitted and is awaiting approval.'
            new_comment.post = the_post
            new_comment.save()
            context['new_comment'] = new_comment
            messages.success(request, message_to_pass)
            response = redirect('post_detail',the_post.slug) # the old redirection (see below) apparently doesn't want to re-include the post part in the template, forcing a redirect seems to fix it. Though i have no idea why.            
            if request.user.is_authenticated :
                response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
                response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
            elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
                response.set_cookie('site_color_mode', 'light', max_age = 5000000)
                response.set_cookie('site_text_color_mode', 'dark', max_age = 5000000)
            return response
    else:
        comment_form = CommentForm()
    if request.user.is_authenticated and not request.user.has_perm('delete'):
        user_comments = Comment.objects.all().filter(author=request.user, active=False, post=the_post)
        if user_comments:
            context['user_inactive_comments'] = user_comments
        context['favorites'] = request.user.favorites.all()
    if request.user.has_perm('delete'):
        moderation_comments = Comment.objects.all().filter(active=False, post=the_post)
        if moderation_comments:
            context['moderation_comments'] = moderation_comments

    context['comment_form'] = comment_form
    response = render(request, template_name, context)
    if request.user.is_authenticated :
        response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
        response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
    elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
        response.set_cookie('site_color_mode', 'light', max_age = 5000000)
        response.set_cookie('site_text_color_mode', 'dark', max_age = 5000000)
    return response


@require_AJAX
def search_posts(request):
    if request.method=='POST':
        posts = Post.objects.all().filter(title__icontains=request.POST['search'])
        posts_by_authors = Post.objects.all().filter(author__pen_name__icontains=request.POST['search'])
        posts_by_authors_username = Post.objects.all().filter(author__username__icontains=request.POST['search'])
        context={
            'post_list' : posts, 
            'posts_by_authors' : posts_by_authors | posts_by_authors_username,
            'search' : True,
        }
        if request.user.is_authenticated :
            context['favorites'] = request.user.favorites.all()
        context['color_mode'] = request.POST['color_mode']
        context['text_color_mode'] = request.POST['text_color_mode']
        if request.POST['search'] == '':
            context['empty'] = True
        html = render_to_string(
            template_name="ajax/index_search_partial.html", context=context)
        data_dict = {"html_from_view":html}
        return JsonResponse(data=data_dict, safe=False)

@login_required
def create_post(request):# turn into class afterwards ?
    template_name = "post/write_post.html"
    books = Book.objects.all().filter(author=request.user)
    form = TextPostForm()
    context = {'form' : form, 'books' : books}
    
    if request.method == 'POST':
        if request.POST['content'] and request.POST['title']:
            new_post = form.save(commit=False)
            new_post.author = request.user
            new_post.title = request.POST['title']
            new_post.content = request.POST['content']
            if request.POST['publish']:
                new_post.status = 1
            new_post.slug = slugify(request.POST['title'])
            if request.POST.get('ischapter'):
                book = get_object_or_404(Book, title=request.POST['book'])
                if not request.POST['position']:
                    messages.error(request, _('Please fill in the chapter!'))
                    return render(request, template_name)
                if Chapter.objects.filter(chapter_position=request.POST['position']).count()>0:
                    messages.error(request, _('A chapter with this number already exists!'))
                    return render(request, template_name)

                new_chapter = Chapter.objects.create(book=book, chapter_position=request.POST['position'], slug=new_post.slug, title=new_post.title, author=new_post.author, content=new_post.content)
                if request.POST['publish']:
                    new_chapter.status = 1
                    messages.success(request, _('Your chapter was published sucessfully'))
                else:
                    messages.success(request, _('Your chapter was saved as a draft'))

                new_chapter.save()
            else:
                if request.POST['publish']:
                    messages.success(request, _('Your post was published sucessfully'))
                else:
                    messages.success(request, _('Your post was saved as a draft'))
                new_post.save()
            response = redirect('/')
            if request.user.is_authenticated :
                response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
                response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
            elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
                response.set_cookie('site_color_mode', 'light', max_age = 5000000)
                response.set_cookie('site_text_color_mode', 'dark', max_age = 5000000)
            return response
    response = render(request, template_name, context)
    if request.user.is_authenticated :
        response.set_cookie('site_color_mode', request.user.color_mode, max_age = 5000000)
        response.set_cookie('site_text_color_mode', set_text_color(request.user.color_mode), max_age = 5000000)
    elif not request.COOKIES.get('site_color_mode'): #checks user cookie for dark mode
        response.set_cookie('site_color_mode', 'light', max_age = 5000000)
        response.set_cookie('site_color_mode', 'dark', max_age = 5000000)
    return response


@require_AJAX
def approve_comment(request):
    if request.user.has_perm('update'):
        if request.method=='POST':
            comment = get_object_or_404(Comment, id=request.POST['id'])
            if not comment.active:
                comment.active = True
                comment.save()
                comments = Comment.objects.all().filter(post=comment.post, active=True)
                context={
                    'comments' : comments,
                    'moderator_ajax_allowed' : True,
                    'darkmode_on' : request.COOKIES.get('site_color_mode')=='dark',
                }
                html = render_to_string(
                    template_name="ajax/comments.html", context=context)
                data_dict = {"html_from_view":html}
                messages.success(request, _('The message was sucessfully approved'))
                response = JsonResponse(data=data_dict, safe=False)
                return response
            messages.error(request, _('This comment has already been approved'))
        response = JsonResponse({"error": "there was an error"})
        response.status_code = 403
    else:
        messages.error(request, _('You shouldn\'t be able to even try that'))
        response = JsonResponse({"error": _("there was an error")})
        response.status_code = 403
    return response
            

@require_AJAX
def delete_comment(request):
    if request.user.has_perm('delete'):
        if request.method=='POST':
            comment = get_object_or_404(Comment, id=request.POST['id'])
            the_post = comment.post
            comment.delete()
            comments = Comment.objects.all().filter(post=the_post, active=True)
            context = {
                'comments' : comments,
                'moderator_ajax_allowed' : True,
                'darkmode_on' : request.COOKIES.get('site_color_mode')=='dark',
                'darkmode_on' : request.COOKIES.get('site_text_color_mode')=='dark',
            }
            html = render_to_string(
                template_name="ajax/comments.html", context=context)
            data_dict = {"html_from_view" : html}
            messages.success(request, _('The message was sucessfully deleted'))
            return JsonResponse(data=data_dict, safe=False)
        response = JsonResponse({"error": _("this comment was already deleted")})
        response.status_code = 403
    else:
        messages.error(request, _('You shouldn\'t be able to even try that'))
        response = JsonResponse({"error": _("there was an error")})
        response.status_code = 403
    return response

def set_color_mode(request):
    if request.method=='GET':
        response = redirect(request.META.get('HTTP_REFERER'))
        if request.GET['site_color_mode']:
            if request.GET['site_color_mode'] in ('light', 'dark'):
                response.set_cookie('site_color_mode', request.GET['site_color_mode'], max_age = 5000000)
                response.set_cookie('site_text_color_mode', set_text_color(request.GET['site_color_mode']), max_age = 5000000)
                if request.user.is_authenticated:
                    this_user = User.objects.get(pk=request.user.pk)
                    this_user.color_mode=request.GET['site_color_mode']
                    this_user.save()
        return response


def set_blursing(request):
    if request.method=='POST':
        response = redirect(request.META.get('HTTP_REFERER'))
        if request.POST['blursed']:
            if request.POST['blursed'] in ('blessed', 'cursed'):
                response.set_cookie('blursed', request.POST['blursed'], max_age = 5000000)
            else:
                response.set_cookie('blursed', 'mundane', max_age = 5000000)
        return response

@require_AJAX
def favorite_view(request):#idk if login_required works properly on ajax calls and i'm too lazy to check
    if request.user.is_authenticated:
        if request.method=='POST':
            the_post = get_object_or_404(Post, id=request.POST['id_post'])
            if the_post in request.user.favorites.all():
                request.user.favorites.remove(the_post)
            else:
                request.user.favorites.add(the_post)
            data_dict = {}
            return JsonResponse(data=data_dict, safe=False)
        response = JsonResponse({"error": _("this comment was already deleted")})
        response.status_code = 403
    else:   
        response = JsonResponse({"error": _("user is being a lil bitch")})
        response.status_code = 403
    return response
