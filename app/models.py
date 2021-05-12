from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


# Create your models here.
class Post(models.Model):
    title          = models.CharField( max_length=50)
    description    = RichTextUploadingField()

    