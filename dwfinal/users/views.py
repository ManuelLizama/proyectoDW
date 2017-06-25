# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout as logout_auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from users.forms import PasswordChangeForm, LoginForm

@login_required
def index(request):
    """
    Pagina inicial.
    """
    return render(
        request,
        'users/index.html',
        {
        }
    )


def login( request ):
    from django.forms.utils import ErrorList
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
