from math import ceil

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
    posts = Post.objects.order_by('-time_create')[:5]
    indx_half_categories = ceil(len(Category.objects.all()) / 2)
    categories_1half = Category.objects.all()[:indx_half_categories]
    categories_2half = Category.objects.all()[indx_half_categories:]
    featured = posts[0]  # The newest post

    context = {
        'title': 'PET Blog',
        'menu': menu,
        'post1': posts[1],
        'post2': posts[2],
        'post3': posts[3],
        'post4': posts[4],
        'featured': featured,
        'categories_1': categories_1half,
        'categories_2': categories_2half
    }
    return render(request, 'blog/index.html', context=context)


def category(request, cat_id):
    posts = Post.objects.filter(category=cat_id).order_by('-time_create')
    context = {
        'title': 'PET Blog',
        'menu': menu,
        'post1': posts[1],
        'post2': posts[1],
        'post3': posts[1],
        'post4': posts[1],
        'featured': posts[0],
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
