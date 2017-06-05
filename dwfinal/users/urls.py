from django.conf.urls import url, include
from users import views

urlpatterns = [
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^$', include('perfil.urls')),
]
