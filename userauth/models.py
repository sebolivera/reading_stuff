from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

COLOR_MODE = (
    ("dark", "Dark Mode"),
    ("light", "Light Mode")
)

class User(AbstractUser):
    pen_name = models.CharField(max_length=254, unique=True, null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    profile_picture = models.ImageField(default=None, null=True, blank=True, upload_to="uploads/")
    favorites = models.ManyToManyField('readwrite.post', default=None, blank=True)
    color_mode = models.CharField(choices=COLOR_MODE, default="light", max_length=100)

    class Meta:
        ordering = ['-pen_name']
