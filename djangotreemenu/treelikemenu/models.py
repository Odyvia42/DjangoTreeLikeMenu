from django.db import models

class Menu(models.Model):
    name = models.CharField('menu_name', max_length=100)
    url = models.URLField('menu_url')

    def __str__(self):
        return str(self.name)

class Submenu(models.Model):
    name = models.CharField('submenu_name', max_length=200)
    parent_menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    url = models.URLField('menu_url')

    def __str__(self):
        return str(self.name)
