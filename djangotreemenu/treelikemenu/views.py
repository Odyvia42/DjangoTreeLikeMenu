from django.shortcuts import render
from .models import Menu


def index(request):
    menus = Menu.objects.all()

    return render(request, 'index.html', {'menus': menus})
