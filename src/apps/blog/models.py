from django.conf import settings
from django.db import models
from django_extensions.db.fields import AutoSlugField
from django_extensions.db import fields as extension_fields
from apps.users.models import User


class BlogCategory(models.Model):
    name = models.CharField(max_length=32)
    class Meta:
        verbose_name_plural = "Categories"
    def __str__(self):
        return self.name

class BlogTag(models.Model):
    name = models.CharField(max_length=32)
    def __str__(self):
        return self.name

class BlogPost(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, editable=False)
    category = models.ForeignKey(BlogCategory, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=64)
    tags = models.ManyToManyField(BlogTag)
    background_image = models.ImageField(upload_to='blogimage')
    slug = extension_fields.AutoSlugField(populate_from='title', blank=True)
    content = models.TextField()
    updated_on = models.DateField(auto_now=True)
    created_on = models.DateField(auto_now_add=True)
    publish_on = models.DateField()
    list_display = ('title', 'category', 'tags', 'author', 'publish_on','created_on','updated_on')
    search_fields = ['title','byline','symbol']
    list_filter = ['publish_on','created_on']
    date_hierarchy = 'pub_date'

    def __str__(self):
        return self.title