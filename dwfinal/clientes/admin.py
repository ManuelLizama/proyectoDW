# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Cliente


admin.site.register(Cliente)
# class ContenedorAdmin(admin.ModelAdmin):
#     """
#         Admin Contenedor
#     """
#     form               = ContenedorForm
#     list_display       = ( 'tipo', 'sucursal', 'producto', 'peso_contenedor_lleno')
#     list_display_links = ( 'tipo', 'sucursal', 'producto')
#     search_fields      = [ 'tipo', 'sucursal', 'producto__nombre' ]