from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/<str:cat_name>', views.index, name='category'),
    path('menu/<str:cat_name>/<str:menu_name>/', views.index, name='menu'),
    path('menu/<str:cat_name>/<str:menu_name>/<str:submenu_name>/', views.index, name='submenu'),
]

