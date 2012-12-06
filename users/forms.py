#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from per_ac.users.models import *
from per_ac.accounts_department.models import *
from django.contrib.auth.models import User

class LoginAddform(forms.Form):
    username = forms.CharField( label = _(u'Имя пользователя'))
    password = forms.CharField( label = _(u'Пароль'),  widget = forms.PasswordInput)

    
class RegAddform(forms.Form):
    username = forms.CharField( label = _(u'Имя пользователя'))
    password = forms.CharField( label = _(u'Пароль'),  widget = forms.PasswordInput)
    email = forms.EmailField( label = _(u'Email'))

    def SaveUser(self, username, email, password):
        user = User.objects.create_user(username, email, password)
        user.is_staf = True
        user.save()
        prof = UserProfile(user=user)
        prof.save()

        safe = Safe(Title = 'Test',  FK_User = user)
        safe.save()
        return user
        
class EditUserForm(forms.Form):
    firstname = forms.CharField( label = _(u'Имя'))
    lastname = forms.CharField( label = _(u'Фамилия'))
    email = forms.EmailField( label = _(u'Email'))
    password = password = forms.CharField( label = _(u'Пароль'),  widget = forms.PasswordInput)
    def SaveChanges(self, user, firstname, lastname, email, password):
        #user = request.User
        user.first_name = firstname
        user.last_name = lastname
        user.email = email
        #user.password = password
        user.save()
