from django.contrib.auth import logout, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, CreateView, FormView
from django.views.generic.detail import SingleObjectMixin

from .form import *
from .models import *
from .utils import DataMixin


class PostHome(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='PET Blog')
        return {**context, **c_def}

    def get_queryset(self):
        return Post.objects.filter(is_published=True)


class CategoryView(DataMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Category: ' + str(context['posts'][0].category))
        return {**context, **c_def}

    def get_queryset(self):
        return Post.objects.filter(category__slug=self.kwargs['cat_slug'], is_published=True)


def contact(request):
    context = {
        'title': 'Contacts',
    }
    return render(request, 'blog/contact.html', context=context)


class CommentFormView(SingleObjectMixin, FormView):
    template_name = 'blog/blogpage.html'
    form_class = CommentForm
    success_url = ''
    model = Post
    slug_url_kwarg = 'post_slug'

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        print(self.get_object().slug)
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('post', kwargs={'post_slug': self.object.slug})


class ShowPost(DetailView):
    model = Post
    template_name = 'blog/blogpage.html'
    context_object_name = 'post'
    slug_url_kwarg = 'post_slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.get_object().title
        context['request'] = self.request
        context['form'] = CommentForm()
        return context


class PostView(View):

    def get(self, request, *args, **kwargs):
        view = ShowPost.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentFormView.as_view()
        form = CommentForm(request.POST)
        # Set the current user
        # to the comment_author field
        form.instance.author = request.user
        # Set the blog post as the current blogpost
        form.instance.post = Post.objects.get(slug=self.kwargs['post_slug'])
        if form.is_valid():
            form.save()
        return view(request, *args, **kwargs)


class AddPost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    form_class = AddPostForm
    template_name = 'blog/add_post.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Post'
        context['request'] = self.request
        return context


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'blog/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Register'
        return context

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'blog/login.html'
    extra_context = {'title': 'Log in'}

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('login')
