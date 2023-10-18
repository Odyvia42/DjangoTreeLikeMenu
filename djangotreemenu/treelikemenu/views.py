from django.shortcuts import render
from .models import Category


def index(request, cat_name=None, menu_name=None, submenu_name=None):
    all_categories = Category.objects.all()
    context = {}
    context['all_categories'] = all_categories
    context['url_parts'] = request.path.replace('/', ' ').split()
    if cat_name:
        cat_name = cat_name[0].upper() + cat_name[1:]
        current_cat = all_categories.get(name=cat_name)
        context['current_cat'] = current_cat
        all_menus = current_cat.menu_set.all()
        context['all_menus'] = all_menus
    if menu_name:
        menu_name = menu_name[0].upper() + menu_name[1:]
        context['current_menu_name'] = all_menus.get(name=menu_name).name
    return render(request, 'index.html', context)
