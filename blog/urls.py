from django.urls import path

from blog.views import *

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>', CategoryView.as_view(), name='category'),
    path('add_post/', AddPost.as_view(), name='add_post')
]
