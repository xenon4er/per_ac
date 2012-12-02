#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from per_ac.accounts_department.models import *
from django.contrib.auth.models import User

import datetime

class CatAddform(forms.Form):
    title = forms.CharField(label = _(u'Название категории'))
    periodicity = forms.IntegerField(label = _(u'Периодизация'))
    def SaveCat(self, title, periodicity, user):
        category = Category(Title = title,  periodicity = periodicity,  FK_User = user)
        category.save()

#filter(FK_User = user)]
class CatEditform(forms.Form):
    category=forms.ModelChoiceField(queryset = Category.objects.none(), required=True)
    def __init__(self, user, *args, **kwargs):
        super(CatEditform, self).__init__(*args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(FK_User = user)
        
class AddPaymentform(forms.Form):
    amount_of_payment = forms.FloatField(label = _(u'Сумма'))
    category=forms.ModelChoiceField(label = _(u'Категория'),queryset = Category.objects.none(), required=True)
    safe=forms.ModelChoiceField(label = _(u'Где хранятся'),queryset = Safe.objects.none(), required=True)
    def __init__(self, request,  user, *args, **kwargs):
        super(AddPaymentform, self).__init__(request, *args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(FK_User = user)
        self.fields['safe'].queryset = Safe.objects.filter(FK_User = user)
    reason = forms.CharField(label = _(u'Причина'))
    def SavePay(self,  user,  pay,  reason, fk_category,  fk_safe, currency):
        date = datetime.date.today()
        payment = Payment(Amount_of_payment = pay, FK_User = user,  Reason = reason,  FK_Category = fk_category, Fk_Safe = fk_safe,  currency = currency,  date = date)
        payment.save()
