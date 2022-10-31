from django.urls import path

from blog.views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', show_post, name='post'),
    path('category/<slug:cat_slug>', category, name='category'),
    path('add_post/', add_post, name='add_post')
]
