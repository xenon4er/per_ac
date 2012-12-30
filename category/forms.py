#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _

from per_ac.accounts_department.models import *
from django.contrib.auth.models import User
from django.forms.extras.widgets import SelectDateWidget
import datetime

class CatAddform(forms.Form):
    title = forms.CharField(label = _(u'Название категории'))
    periodicity = forms.IntegerField(label = _(u'Периодизация'))
    def SaveCat(self, title, periodicity, user):
        category = Category(Title = title,  periodicity = periodicity,  FK_User = user)
        category.save()

#filter(FK_User = user)]
class CatEditform(forms.Form):
    title = forms.CharField(label = _(u'Название категории'))
    periodicity = forms.IntegerField(label = _(u'Периодизация'))
    
    def SaveChanges(self, catname, newtitle, newperiodicity, user):
        cat = Category.objects.filter(FK_User = user, Title = catname)
        cat1 = cat[0]
        print newtitle
        cat1.Title = newtitle
        cat1.periodicity = newperiodicity
        print cat1.Title
        cat1.save()

class AddPaymentform(forms.Form):
    amount_of_payment = forms.FloatField(label = _(u'Сумма'))
    category=forms.ModelChoiceField(label = _(u'Категория'),queryset = Category.objects.none(), required=True)
    safe=forms.ModelChoiceField(label = _(u'Где хранятся'),queryset = Safe.objects.none(), required=True)
    reason = forms.CharField(label = _(u'Причина'))
    def __init__(self, request,  user, *args, **kwargs):
        super(AddPaymentform, self).__init__(request, *args, **kwargs)
        self.fields['category'].queryset = Category.objects.filter(FK_User = user)
        self.fields['safe'].queryset = Safe.objects.filter(FK_User = user)
    
    def SavePay(self,  user,  pay,  reason, fk_category,  fk_safe, currency):
        date = datetime.date.today()
        payment = Payment(Amount_of_payment = pay, FK_User = user,  Reason = reason,  FK_Category = fk_category, Fk_Safe = fk_safe,  currency = currency,  date = date)
        payment.save()

class Historyform(forms.Form):
    years_choices = []
    month_choise = []
    #month_choise .append([])
    i =1
    while i < 13 :
        month_choise.append([i, i])
        i = i +1
   
    months=forms.ChoiceField(label = _(u'Месяц'),choices = month_choise , required=True)
    years=forms.ChoiceField(label = _(u'Год'),choices = years_choices, required=True)
    def __init__(self, request, user,  *args,  **kwargs):
        super(Historyform, self).__init__(request, *args,  **kwargs)
        yearslist = []
        #yearslist.append([])
        yearslist.append([user.date_joined.year, user.date_joined.year])
        y = 1
        while y <= (datetime.date.today().year - user.date_joined.year):
            yearslist.append([user.date_joined.year + y, user.date_joined.year + y])
            y = y +1
        self.fields['years'].choices = yearslist
