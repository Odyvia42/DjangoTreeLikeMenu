from django.contrib import admin
from .models import Menu

class MenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'url', 'id')
admin.site.register(Menu, MenuAdmin)