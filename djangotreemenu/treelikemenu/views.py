from django.shortcuts import render
from .models import Menu, Category

def index(request, cat_name=None, menu_name=None, submenu_name=None):
    all_menus = Menu.objects.all()
    all_categories = Category.objects.all()
    current_url = request.path
    url_parts = current_url.replace('menu', ' ').replace('/', ' ').split()
    page_name = ' '.join(url_parts)
    context = {'all_menus': all_menus,
        'current_url': current_url,
        'all_categories': all_categories,
        'page_name': page_name,
        }

    if cat_name:
        current_category = all_categories.get(name=cat_name)
        context['current_category'] = current_category
        menus = all_menus.filter(parent_category=current_category)
        context['menus'] = menus

    if menu_name:
        current_menu = all_menus.get(name=menu_name)
        previous_menus = []
        for i in range(1, current_menu.id):
            menu_to_check = all_menus.get(id=i)
            if menu_to_check.parent_category.id == current_category.id:
                previous_menus.append(menu_to_check)
        context['current_menu'] = current_menu
        context['previous_menus'] = previous_menus



    return render(request, 'index.html', context)


