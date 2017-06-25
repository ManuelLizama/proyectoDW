# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from .forms import ClienteForm
from users import views
from clientes.models import Cliente


@login_required
def nuevo_cliente_view(request):
    if request.POST:
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success( request, 'Cliente creado correctamente.' )
            return redirect( reverse( views.index ) )
    else:
        form = ClienteForm()
    return render(request, 'clientes/nuevo_cliente.html', {'form' : form})


@login_required
def lista_cliente( request ):
    clientes = Cliente.objects.all()
    return render(
        request,
        'clientes/lista_clientes.html',
        {
            'clientes' : clientes
        }
    )