from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import BlogPost

class BlogPostCreateForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = BlogPost
        fields = ('title', 'category', 'tags', 'background_image', 'content', 'publish_on')