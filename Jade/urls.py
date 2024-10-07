from django.contrib import admin
from django.urls import  path
from .views import inicio , mostrar_producto, filtro_por_fecha

urlpatterns = [
    path("",  inicio, name="home"),
    path("productos/" , mostrar_producto, name="productos"),
    path('filtro/', filtro_por_fecha, name='filtro'),
]