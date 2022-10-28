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


@register.inclusion_tag('blog/template_tags/navbar.html')
def responsive_navbar(title):
    menu = [
        {'title': 'PET Blog', 'url_name': 'home'},
        {'title': 'About', 'url_name': 'about'},
        {'title': 'Contacts', 'url_name': 'contact'},
        {'title': 'Log in', 'url_name': 'login'},
    ]
    return {'menu': menu, 'title': title}
