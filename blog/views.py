from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView

from .form import *
from .models import *


class PostHome(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        context['title'] = 'PET Blog'
        context['featured'] = posts[0]
        context['row_posts'] = [posts[1:][i:i + 2] for i in range(0, len(posts[1:]), 2)]  # Breaking posts into pairs first post for featured
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


# def index(request):
#     posts = Post.objects.order_by('-time_create')
#     row_posts = [posts[1:][i:i + 2] for i in
#                  range(0, len(posts[1:]), 2)]  # Breaking posts into pairs first post for featured
#     featured = posts[0]  # The newest post
#
#     context = {
#         'title': 'PET Blog',
#         'row_posts': row_posts,
#         'featured': featured,
#     }
#     return render(request, 'blog/index.html', context=context)


def category(request, cat_slug):
    category = Category.objects.get(slug=cat_slug).pk  # Get categoru pk for filter
    posts = Post.objects.filter(category=category).order_by('-time_create')
    row_posts = [posts[1:][i:i + 2] for i in range(0, len(posts[1:]), 2)]
    featured = posts[0]
    context = {
        'title': 'PET Blog',
        'row_posts': row_posts,
        'featured': featured,
    }
    if len(posts) == 0:
        raise Http404

    return render(request, 'blog/index.html', context=context)


def about(request):
    context = {
        'title': 'About',
    }
    return render(request, 'blog/about.html', context=context)


def contact(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'blog/contact.html', context=context)


def login(request):
    context = {
        'title': 'Log in',
    }
    return render(request, 'blog/login.html', context=context)


def show_post(request, post_slug):
    post = get_object_or_404(Post, slug=post_slug)
    context = {
        'title': post.title,
        'post': post,

    }
    return render(request, 'blog/blogpage.html', context=context)


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddPostForm()

    context = {
        'title': 'Add Post',
        'form': form
    }
    return render(request, 'blog/add_post.html', context=context)
