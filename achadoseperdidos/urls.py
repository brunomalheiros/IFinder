from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='index'),
    path('lista-de-itens', views.listadeitens, name='lista-de-itens'),
    path('adicionar-item', views.adicionaritem, name='adicionar-item'),
]