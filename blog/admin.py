from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'time_create', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['id', 'name']
    search_fields = ['name']


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoriesAdmin)
