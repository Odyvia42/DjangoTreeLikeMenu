from django.contrib import admin
from .models import Menu, Category

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    fields = ['name', 'url', 'parent_menu', 'parent_category']
    list_display = ['__str__', 'name', 'url', 'parent_menu', 'parent_category', 'id']

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    fields = ['name']
    list_display = ['__str__', 'name', 'id']