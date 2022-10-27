from django.shortcuts import render
from .models import *

menu = [
    {'title': 'PET Blog', 'url_name': 'home'},
    {'title': 'About', 'url_name': 'about'},
    {'title': 'Contacts', 'url_name': 'contact'},
    {'title': 'Log in', 'url_name': 'login'},
]


def index(request):
    posts = Post.objects.all()
    context = {
        'title': 'PET Blog',
        'menu': menu,
        'posts': posts
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


def page(request):
    return render(request, 'blog/blogpage.html')
