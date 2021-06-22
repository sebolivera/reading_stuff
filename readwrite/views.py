from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.views.generic import TemplateView
from .models import Post, Comment, Book, Chapter, Author
from .forms import CommentForm, PostForm
from django.contrib.auth import logout, login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.utils.text import slugify

# Create your views here.

class IndexView(TemplateView):
    template_name = "index.html"
    context = {'post_list' : Post.objects.all()}

    def get(self, request):
        return render(request, self.template_name, self.context)


def postDetail(request, slug): # not a class bc post & get annoying
    template_name = "post/post.html"
    the_post = get_object_or_404(Post, slug=slug)
    comments = the_post.comments.filter(active=True)
    context = {'post' : the_post, 'comments' : comments}
    new_comment = None

    if request.method == 'POST' and request.user.is_authenticated:
        context = {'post' : the_post}
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False) # doesn't add it to the db as we need to link the post
            new_comment.user = request.user
            if hasattr(request.user, "administrator"):
                request.active = True
            new_comment.POST = the_post
            new_comment.save()
            context['new_comment'] = new_comment
            messages.success(request, 'Your comment has been successfully posted!')
    else:
        comment_form = CommentForm()
    if request.user.is_authenticated:
        user_comments = Comment.objects.all().filter(user=request.user, active=False, post=the_post)
        if user_comments:
            context['user_inactive_comments'] = user_comments

    context['comment_form'] = comment_form
    return render(request, template_name, context)

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out sucessfully. Now scram.')
    return redirect('/')

def login_view(request):
    template_name = "registration/login.html"
    form = AuthenticationForm()
    context = {'form' : form}
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Log in sucessful. Welcome Traveler.')
            return redirect('/')
        else:
            return redirect('login')
    elif request.method == 'GET' :
        return render(request, template_name, context)

def password_reset_view(request): #todo
    return HttpResponse("forgot to implement that one, mb")

@login_required
def create_post(request):
    template_name = "post/write_post.html"
    books = Book.objects.all().filter(author=request.user)
    form = PostForm()
    context = {'form' : form, 'books' : books}
    
    if request.method == 'POST':
        if request.POST['content'] and request.POST['title']:
            new_post = form.save(commit=False)
            new_post.author = Author.objects.get(id=request.user.id)
            new_post.title = request.POST['title']
            new_post.content = request.POST['content']
            if request.POST['publish']:
                new_post.status = 1
            new_post.slug = slugify(request.POST['title'])
            if request.POST['ischapter']:
                book = get_object_or_404(Book, title=request.POST['book'])
                if not request.POST['position']:
                    messages.error(request, 'Please fill in the chapter!')
                    return render(request, template_name)
                if Chapter.objects.filter(chapter_position=request.POST['position']).count()>0:
                    messages.error(request, 'A chapter with this number already exists!')
                    return render(request, template_name)

                new_chapter = Chapter.objects.create(book=book, chapter_position=request.POST['position'], slug=new_post.slug, title=new_post.title, author=new_post.author, content=new_post.content)
                print("i got this:",request.POST['publish'])
                if request.POST['publish']:
                    new_chapter.status = 1
                    messages.success(request, 'Your chapter was published sucessfully')
                else:
                    messages.success(request, 'Your chapter was saved as a draft')

                new_chapter.save()
            else:
                if request.POST['publish']:
                    messages.success(request, 'Your post was published sucessfully')
                else:
                    messages.success(request, 'Your post was saved as a draft')
                new_post.save()
            return redirect('/')
    return render(request, template_name, context)