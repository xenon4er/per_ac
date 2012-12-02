from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from per_ac.accounts_department.models import *

from django.template import RequestContext
from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect

from django.views.generic.simple import direct_to_template
from forms import *


#from django.views.decorators.csrf import csrf_protec

@csrf_protect
def AddCat(request):
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect('/registr/')
    errors = []
    count_user = User.objects.count()
    
    form = CatAddform(request.POST or None)
    context = { 'form': form,  'errors':errors, 'count_user':count_user}
    
    if request.method == 'POST' and form.is_valid():
        title = form.cleaned_data.get('title',  None)
        periodicity = form.cleaned_data.get('periodicity', None)
        category = form.SaveCat(title,  periodicity, user)
        return HttpResponseRedirect('/view_cat/')

    return direct_to_template(request, 'new_category.html', context)

def ViewCat(request):
    user = request.user
    count_user = User.objects.count()
    if not user.is_authenticated():
        return HttpResponseRedirect('/registr/')
    catlist = Category.objects.filter(FK_User = request.user)
    return render_to_response('category.html', {'cat':catlist, 'user':user, 'count_user':count_user})

def EditCat(request):
    user = request.user
    count_user = User.objects.count()
    if not user.is_authenticated():
        return HttpResponseRedirect('/registr/')
    errors = []
    form = CatEditform(user)
    form1 = CatAddform(request.POST)
    context = { 'form': form,'form1':form1,   'errors':errors, 'count_user':count_user}

    return direct_to_template(request, 'edit_category.html', context)
@csrf_protect
def AddPayment(request):
    count_user = User.objects.count()
    user = request.user
    if not user.is_authenticated():
        return HttpResponseRedirect('/registr/')
    errors = []
    pay = Payment.objects.all()
    cat = Category.objects.all()
    form = AddPaymentform(request.POST, user)
    context = { 'form': form, 'errors':errors, 'tables': pay, 'category':cat, 'count_user':count_user}
    
    
    if  request.method == 'POST' and form.is_valid():
        amount_of_payment = form.cleaned_data.get('amount_of_payment', None)
        reason = form.cleaned_data.get('reason', None)
        currency = "rub"
        fk_category = Category.objects.filter(id = form.data['category'])[0]
        fk_safe = Safe.objects.filter(id = form.data['safe'])[0]
        payment = form.SavePay(user, amount_of_payment, reason, fk_category,fk_safe ,currency)
    return direct_to_template(request, 'add_payment.html', context)
