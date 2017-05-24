# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from base.views import index
from users.forms import PasswordChangeForm, LoginForm
from usercliente.views import cartola


@login_required
def index(request):
    """
    Pagina inicial con últimos cambios realizados por el usuario.
    """
    revs = Version.objects.filter( content_type__model__in = ( 'ordentrabajo' , 'solicitud', 'contrato', 'respaldofactura', 'archivo' ), revision__in = Revision.objects.filter( user = request.user ) ).order_by('-revision__date_created')
    paginator = Paginator(revs, 25)  # Show 25 contacts per page
    page = request.GET.get('page') or 1

    if request.user.es_cliente:
        if 'sucursales' not in request.session:
            sucursales = Direccion.objects.filter( cliente = request.user.clientes.all().first() )
            request.session['sucursales'] = [s.id for s in sucursales]

    try:
        revisiones = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        revisiones = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        revisiones = paginator.page(paginator.num_pages)

    return render(
        request,
        'base/index.html',
        {
            'revisiones' : revisiones
        }
    )


def login( request ):
    from django.forms.util import ErrorList
    if request.user.is_authenticated():
        return redirect(index)
    if request.method == "POST":
        form = LoginForm( request.POST )
        if form.is_valid():
            user = authenticate( username = form.cleaned_data['username'], password = form.cleaned_data['password'] )
            if user is not None:
                if user.is_active:
                    # Clave correcta, y el usuario está marcado "activo"
                    auth_login(request, user)
                    return redirect(index)
            else:
                errors = form._errors.setdefault("__all__", ErrorList())
                errors.append(u"Usuario desactivado")
        else:
            errors = form._errors.setdefault("__all__", ErrorList())
            errors.append(u"Nombre de usuario y / ó contraseña incorrectos")
    else:
        form = LoginForm()
    return render(
        request,
        'users/login.html',
        {
            'form' : form,
        }
    )


@login_required
def logout( request ):
    logout_auth(request)
    messages.info(request, 'Sesión finalizada.')
    return redirect(index)


@login_required
def listar( request ):
    usuarios = User.objects.all()
    return render(
        request,
        'users/listar.html',
        {
            'usuarios' : usuarios
        }
    )


@login_required
def passwordChange(request):
    if request.method == 'POST':
        form = PasswordChangeForm( request.user, request.POST )
        if form.is_valid():
            form.save()
            messages.success( request, 'Contraseña cambiada con éxito' )
            return redirect(index)
    else:
        form = PasswordChangeForm(request.user)
    return render(
        request,
        'users/password_change.html',
        locals()
    )
