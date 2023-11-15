#from django.conf.urls import urls
from django.urls import path,include
from . import views
urlpatterns = [
    path('index', views.index, name='index'),
    path('quienes_somos', views.quienes_somos, name='quienes_somos'),
    path('producto', views.producto, name='producto'),
    path('validar', views.validar, name='validar'),
    path('login', views.login, name='login'),
    path('cerrar', views.cerrar, name='cerrar'),
    path('crud_usuarios', views.crud_usuarios, name='crud_usuarios'),
    path('usuario_añadir', views.usuario_añadir, name='usuario_añadir'),
    path('usuario_eliminar/<str:pk>', views.usuario_eliminar, name='usuario_eliminar'),
    path('usuario_editar/<str:pk>', views.usuario_editar, name='usuario_editar'),
    path('usuario_actualizar', views.usuario_actualizar, name='usuario_actualizar'),
    path('comprar/<str:pk>', views.comprar, name='comprar'),
]
