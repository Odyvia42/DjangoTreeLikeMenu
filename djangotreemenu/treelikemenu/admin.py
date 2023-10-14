from django.contrib import admin
from .models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    fields = ['name', 'url', 'parent_menu']
    list_display = ['__str__', 'name', 'url', 'parent_menu', 'id']

