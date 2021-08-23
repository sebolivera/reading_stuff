from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

DEFAULT_AUTHOR = 1

class Book(models.Model):
    title = models.CharField(max_length=254)
    position = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('userauth.user', default=DEFAULT_AUTHOR, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=254)
    slug = models.SlugField(max_length=254, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = RichTextField()
    status = models.IntegerField(choices=STATUS, default=0)
    author = models.ForeignKey('userauth.user', default=DEFAULT_AUTHOR, on_delete=models.CASCADE) #redundancy w/ book, but what about the case where a book has no chapters? idk leave me alone

    class Meta:
        ordering = ['-created_on']
   
    def __str__(self):
        return self.title

class Chapter(Post):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    chapter_position = models.CharField(max_length=40)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey('userauth.user', on_delete=models.CASCADE)
    body = RichTextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)
    edited = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment {} by {}'.format(self.body, self.user.username)
