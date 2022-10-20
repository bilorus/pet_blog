from django.contrib import admin

from .models import *


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'category', 'time_create', 'is_published']
    list_display_links = ['id', 'title']
    search_fields = ['title', 'text']


admin.site.register(Post, PostAdmin)
admin.site.register(Category)
