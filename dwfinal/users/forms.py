# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from django.contrib.auth.models import User,Group


class LoginForm(forms.Form):
    """
        Formulario que registra las credenciales de un usuario
    """
    username = forms.CharField( label = ( "Nombre de Usuario" ) )  # widget = forms.PasswordInput
    password = forms.CharField( label = ( "Contraseña" ), widget = forms.PasswordInput )  # widget = forms.PasswordInput

    def clean_username(self):
        """
            Validador Nombre de Usuario
        """
        username = self.cleaned_data.get('username')
        if len(username) < 3:
            raise forms.ValidationError("Nombre de usuario debe contener al menos 3 caracteres.")
        else:
            return username

    def clean_password(self):
        """
            Validador Password
        """
        password = self.cleaned_data.get('password')
        if len(password) < 3:
            raise forms.ValidationError(u'La contraseña debe contener al menos 3 caracteres')
        else:
            return password

    def clean(self):
        """
            Validador del Formulario
        """
        return self.cleaned_data


class SetPasswordForm(forms.Form): 
    """ 
    A form that lets a user change set his/her password without 
    entering the old password 
    """ 
    new_password1 = forms.CharField( label = ("Nueva Contraseña"), widget = forms.PasswordInput(attrs={'class':'form-control'}) )
    new_password2 = forms.CharField( label = ("Confirme Contraseña"), widget = forms.PasswordInput(attrs={'class':'form-control'}) ) 

    def clean_new_password2(self): 
        password1 = self.cleaned_data.get('new_password1') 
        password2 = self.cleaned_data.get('new_password2') 
        if password1 and password2: 
            if password1 != password2: 
                raise forms.ValidationError("Las contraseñas no coinciden por favor escribalas nuevamente.")
            return password2 
    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1']) 
        if commit: 
            self.user.save() 
        return self.user

class PasswordChangeForm(SetPasswordForm): 
    """ 
    A form that lets a user change his/her password by entering 
    their old password. 
    """ 
    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(PasswordChangeForm, self).__init__(*args, **kwargs)
    old_password = forms.CharField( label = ("Contraseña actual"), widget = forms.PasswordInput(attrs={'class':'form-control'}) ) 
    def clean_old_password(self): 
        """ 
        Validates that the old_password field is correct. 
        """ 
        old_password = self.cleaned_data["old_password"] 
        if not self.user.check_password(old_password): 
            raise forms.ValidationError("La contraseña ingresada no es correcta intente nuevamente.") 
        return old_password