"""training_portal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.urls import path
from apps.blog.views import home #, BlogPostCreateFormView
from apps.blog import views

app_name = 'blog'
urlpatterns = [
    path('', home, name='home'),
    path('posts/create', views.blog_post_create),#BlogPostCreateFormView.as_view()),
    path('posts/<int:post_id>/', views.detail_blog_post),
]
