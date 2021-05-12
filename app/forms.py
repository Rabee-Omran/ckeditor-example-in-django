from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from app.models import Post


class PostForm(forms.ModelForm):
    description = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = ['title', 'description']
