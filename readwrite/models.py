from django.db import models
from django.contrib.auth.models import User
# Create your models here.

STATUS = (
    (0, "Draft"),
    (1, "Published")
)

DEFAULT_AUTHOR = 1

class Author(User):
    pen_name = models.CharField(max_length=255, unique=True)

    class Meta:
        ordering = ['-pen_name']

class Book(models.Model):
    title = models.CharField(max_length=255)
    position = models.FloatField()
    created_on = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(Author, default=DEFAULT_AUTHOR, on_delete=models.CASCADE)

class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ['-created_on']
    
    def __str__(self):
        return self.title

class Chapter(Post):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.ForeignKey(Author, default=DEFAULT_AUTHOR, on_delete=models.CASCADE) #redundancy w/ book, but what about the case where a book has no chapters? idk leave me alone

