from django.contrib import admin
from .models import Menu, Submenu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
admin.site.register(Menu, MenuAdmin)

class SubMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id', 'parent_menu')
admin.site.register(Submenu, SubMenuAdmin)