from django.contrib import admin
from .models import BlogCategory
from .models import BlogTag
from .models import BlogPost

admin.site.register(BlogCategory)
admin.site.register(BlogTag)
admin.site.register(BlogPost)