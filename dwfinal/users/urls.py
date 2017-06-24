from django.conf.urls import url
from users import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^$', views.listar, name='usuarios'),
]
