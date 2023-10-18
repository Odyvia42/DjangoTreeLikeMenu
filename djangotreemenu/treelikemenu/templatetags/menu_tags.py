from django import template
from django.template import RequestContext

register = template.Library()


@register.inclusion_tag('../templates/menu.html', takes_context=True)
def draw_menu(context: RequestContext, cat_name=None):
    # defining the local context
    menu_context = {}

    # getting needed data from the context
    current_category = context['current_cat']
    url_parts = context['url_parts']
    all_menus = context['all_menus']
    menu_context['all_menus'] = all_menus

    # collecting the top level menu items
    top_level_items = []
    for item in all_menus:
        if not item.parent_menu:
            top_level_items.append(item)
    menu_context['top_level_items'] = top_level_items

    # collecting child items for each top level item
    children = {}
    for item in top_level_items:
        if item.get_children():
            children[item.name] = item.get_children()
    menu_context['children'] = children

    # collecting all the items preceding the currently active item
    previous_menus = []
    if 'current_menu_name' in context:
        current_menu_name = context['current_menu_name']
        if current_menu_name.lower() in url_parts:
            current_menu = all_menus.get(name=current_menu_name)
            menu_context['current_menu'] = current_menu
            menus_to_check = all_menus.filter(id__lte=current_menu.id)
            for item in menus_to_check:
                if item.parent_category == current_category:
                    previous_menus.append(item)
    menu_context['previous_menus'] = previous_menus

    # obtaining the human-readable name of the page
    menu_context['url_parts'] = context['url_parts']
    page_name = []
    for i in context['url_parts']:
        i = i[0].upper() + i[1:]
        page_name.append(i)
    menu_context['page_name'] = ' '.join(page_name)

    return menu_context


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)
