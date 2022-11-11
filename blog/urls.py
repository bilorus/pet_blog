from django.urls import path

from blog.views import *

urlpatterns = [
    path('', PostHome.as_view(), name='home'),
    path('contact/', contact, name='contact'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('post/<slug:post_slug>', PostView.as_view(), name='post'),
    path('category/<slug:cat_slug>', CategoryView.as_view(), name='category'),
    path('add_post/', AddPost.as_view(), name='add_post')
]
