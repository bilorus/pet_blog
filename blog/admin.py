from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category', 'time_create', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'text')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'time_create')
    prepopulated_fields = {'slug': ('title',)}


class CategoriesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoriesAdmin)
