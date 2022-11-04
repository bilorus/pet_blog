from django import template

from blog.models import *

register = template.Library()


@register.inclusion_tag('blog/template_tags/cat_widget.html')
def categories_widget():
    cats = Category.objects.all()
    return {'cats': cats}


@register.inclusion_tag('blog/template_tags/navbar.html')
def responsive_navbar(title, request):
    menu = [
        {'title': 'PET Blog', 'url_name': 'home'},
        {'title': 'Add Post', 'url_name': 'add_post'},
        {'title': 'Contacts', 'url_name': 'contact'},
    ]
    menu_user_not_login = [
        {'title': 'Register', 'url_name': 'register'},
        {'title': 'Log in', 'url_name': 'login'}]
    menu_user_login = [
        {'title': request.user.username, 'url_name': 'home'},
        {'title': 'Log out', 'url_name': 'logout'},
    ]
    return {'menu': menu, 'title': title, 'request': request, 'user_in': menu_user_login,
            'user_out': menu_user_not_login}
