from django.shortcuts import render
from .models import Menu, Submenu


def index(request):
    menus = Menu.objects.all()
    submenus = Submenu.objects.all()
    return render(request, 'index.html', {'menus': menus, 'submenus': submenus})
