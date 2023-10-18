from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^(?P<cat_name>[a-zA-Z]*)/$', views.index, name='category'),
    re_path(r'^(?P<cat_name>[a-zA-Z]*)/(?P<menu_name>[a-zA-Z]*)/$', views.index, name='menu'),
    re_path(r'^(?P<cat_name>[a-zA-Z]*)/(?P<menu_name>[a-zA-Z]*)/(?P<submenu_name>[0-9a-zA-Z]*)/$',
            views.index, name='submenu'),
]
