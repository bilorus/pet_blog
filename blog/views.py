from django.shortcuts import render
from .models import *

menu = [
    {'title': 'PET Blog', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]


def index(request):
    posts = Post.objects.order_by('-time_create')[1:5]
    featured = Post.objects.get(pk=7)
    context = {
        'title': 'PET Blog',
        'menu': menu,
        'post1': posts[0],
        'post2': posts[1],
        'post3': posts[2],
        'post4': posts[3],
        'featured': featured
    }
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
