from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView

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
        context['row_posts'] = [posts[1:][i:i + 2] for i in
                                range(0, len(posts[1:]), 2)]  # Breaking posts into pairs first post for featured
        return context

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class CategoryView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        posts = self.get_queryset()
        context['title'] = 'Category: ' + str(context['posts'][0].category)
        context['featured'] = posts[0]
        context['row_posts'] = [posts[1:][i:i + 2] for i in
                                range(0, len(posts[1:]), 2)]  # Breaking posts into pairs first post for featured
        return context

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


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


class ShowPost(DetailView):
    model = Post
    template_name = 'blog/blogpage.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        return context


class AddPost(CreateView):
    form_class = AddPostForm
    template_name = 'blog/add_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Post'
        return context
