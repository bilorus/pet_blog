from django import template
from blog.models import *

register = template.Library()


@register.simple_tag()
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('blog/template_tags/cat_widget.html')
def categories_widget():
    cats = Category.objects.all()
    return {'cats': cats}