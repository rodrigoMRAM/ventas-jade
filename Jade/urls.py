from django.contrib import admin
from django.urls import  path
from .views import inicio , mostrar_producto, filtro_por_fecha, ProductoUpdate, agregar_producto , EliminarProducto, ultimo_producto

urlpatterns = [
    # path("",  inicio, name="home"),
    path("" , mostrar_producto, name="productos"),
    path("agregar/" , agregar_producto, name="agregar"),
    path('filtro/', filtro_por_fecha, name='filtro'),
    path('ultimo_producto/', ultimo_producto, name='ultimo_producto'),
    path(r'^editar/(?P<pk>\d+)$', ProductoUpdate.as_view(), name="editar"),
    path("productos/<pk>/delete" ,EliminarProducto.as_view(),name="eliminar"),
    

]