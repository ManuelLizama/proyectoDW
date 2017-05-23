# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def prueba_view(request):

    saludo = 'Hola diego'
    equipo = ['Manuel', 'JT', 'Diego']
    return render(request,'perfil/prueba.html',
            {'saludo':saludo,
            'equipo': equipo,
            }
            )

def prueba2_view(request):

    saludo = 'Hola CTM'
    equipo = ['Alberto', 'Patricia', 'Emiliano']
    return render(request,'perfil/prueba.html',
            {'saludo':saludo,
            'equipo': equipo,
            }
            )