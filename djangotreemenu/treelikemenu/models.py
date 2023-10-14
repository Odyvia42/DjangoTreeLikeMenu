from django.db import models

class Menu(models.Model):
    name = models.CharField('menu_name', max_length=100)
    url = models.URLField('menu_url')
    parent_menu = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, default=0)

    def __str__(self):
        return str(self.name)

    def get_children(self):
        return self.menu_set.all()



