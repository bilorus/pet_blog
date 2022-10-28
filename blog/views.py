from django.http import Http404
from django.shortcuts import render

from .models import *

menu = [
    {'title': 'PET Blog', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]


def index(request):
    posts = Post.objects.order_by('-time_create')
    row_posts = [posts[1:][i:i + 2] for i in
                 range(0, len(posts[1:]), 2)]  # Breaking posts into pairs first post for featured
    featured = posts[0]  # The newest post

    context = {
        'title': 'PET Blog',
        'menu': menu,
        'row_posts': row_posts,
        'featured': featured,
    }
    return render(request, 'blog/index.html', context=context)


def category(request, cat_id):
    posts = Post.objects.filter(category=cat_id).order_by('-time_create')
    row_posts = [posts[1:][i:i + 2] for i in range(0, len(posts[1:]), 2)]
    featured = posts[0]
    context = {
        'title': 'PET Blog',
        'menu': menu,
        'row_posts': row_posts,
        'featured': featured,
    }
    if len(posts) == 0:
        raise Http404

    return render(request, 'blog/index.html', context=context)


def about(request):
    context = {
        'title': 'About',
        'menu': menu
    }
    return render(request, 'blog/about.html', context=context)


def contact(request):
    context = {
        'title': 'Contacts',
        'menu': menu
    }
    return render(request, 'blog/contact.html', context=context)


def login(request):
    context = {
        'title': 'Log in',
        'menu': menu
    }
    return render(request, 'blog/login.html', context=context)


def show_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    context = {
        'title': post.title,
        'menu': menu,
        'post': post,

    }
    return render(request, 'blog/blogpage.html', context=context)
