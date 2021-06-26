from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

DEFAULT_AUTHOR = 1

class User(AbstractUser):
    pen_name = models.CharField(max_length=254, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    profile_picture = RichTextUploadingField(default=None, null=True, blank=True)

    class Meta:
        ordering = ['-pen_name']

class Book(models.Model):
    title = models.CharField(max_length=254)
    position = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, default=DEFAULT_AUTHOR, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey(User, default=DEFAULT_AUTHOR, on_delete=models.CASCADE) #redundancy w/ book, but what about the case where a book has no chapters? idk leave me alone

    class Meta:
        ordering = ['-created_on']
   
    def __str__(self):
        return self.title

class Chapter(Post):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_position = models.CharField(max_length=40)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
