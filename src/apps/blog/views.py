from django.shortcuts import render
from django.contrib.auth import logout
from django.views.generic import CreateView, UpdateView
from .models import BlogPost
from .forms import BlogPostCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from apps.users.models import User

def home(request):
    posts = BlogPost.objects.all().order_by('-publish_on')
    return render(request, 'blog/index.html', {'posts': posts})

def detail_blog_post(request, post_id):
    post = BlogPost.objects.get(pk=post_id)
    return render(request, 'blog/contents-detail.html', {'post': post})

# class BlogPostCreateFormView(LoginRequiredMixin, CreateView):
#     model = BlogPost
#     form_class = BlogPostCreateForm
#     template_name = "loggedInPages/portalPostCreate.html"
#     success_url = "/blog"

@login_required
def blog_post_create(request):
    p = BlogPost(author=User.objects.get(pk=request.user.id))
    form = BlogPostCreateForm(request.POST or None, instance=p)
    form.save(commit=False)
    if form.is_valid():
        name = form.cleaned_data['name']
        text    = form.cleaned_data['text']

        form.save()
        return HttpResponseRedirect('/blog')
    else:
        return render(request, 'loggedInPages/portalPostCreate.html', {'form': form})