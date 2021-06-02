from django import template
from women.models import *

register = template.Library()

@register.simple_tag(name='getcats')
def get_categories():
    return Category.objects.all()

@register.inclusion_tag('women/list_categories.html')
def show_categories(sort=None, cat_selected=0):
    if not sort:
        cats = Category.objects.all()
    else:
        cats = Category.objects.all(sort)
    return {'cats': cats, 'cat_selected': cat_selected}

@register.inclusion_tag('women/list_menu.html')
def show_menu():
        menu = [{'title': 'About', 'url_name': 'about'},
                {'title': 'Add an article', 'url_name': 'add_page'},
                {'title': 'Contact', 'url_name': 'contact'},
                {'title': 'Log in', 'url_name': 'login'}
                ]
        return {'menu': menu}