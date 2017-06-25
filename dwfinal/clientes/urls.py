from django.conf.urls import url
from clientes import views

urlpatterns = [
    url(r'^nuevocliente/$', views.nuevo_cliente_view, name='nuevo_cliente'),
    url(r'^lista_clientes/$', views.lista_cliente, name='lista_cliente'),
]
