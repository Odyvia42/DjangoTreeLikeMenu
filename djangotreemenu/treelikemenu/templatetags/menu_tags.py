from django import template
from ..models import Menu

register = template.Library()

@register.inclusion_tag('../templates/menu.html', takes_context=True)
def draw_menu(context, menu_name):
    current_menu = Menu.objects.get(name=menu_name)
    children = current_menu.get_children()

    return {'current_menu': current_menu, 'children': children}


def get_subchildren(menu_name):
    current_menu = Menu.objects.get(name=menu_name)
    submenus = current_menu.get_children()
    return{'submenus', submenus}