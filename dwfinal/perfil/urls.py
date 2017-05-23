# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from . import views
admin.autodiscover()

urlpatterns = [
    url(r'^prueba/', views.prueba_view),
    url(r'^osos/', views.prueba2_view),
]