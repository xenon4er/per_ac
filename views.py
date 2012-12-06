from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from per_ac.accounts_department.models import *
from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect

def welcome(request):
    user = request.user
    count_user = User.objects.count()
    
    my_savings = 0.0
    
    if request.user.is_authenticated():
        u_pay = Payment.objects.filter(FK_User = user)
        for x in u_pay:
           my_savings += x.Amount_of_payment
    
    return render_to_response('welcome.html',{'user':user, 'count_user':count_user, 'my_savings' : my_savings})

def main_menu(request):
    count_user = User.objects.count()
    my_savings = 0.0
    
    if request.user.is_authenticated():
        uname = request.user.username
        #ubalance = "dsf"#request.user.balance
        qq = request.user.get_profile()
        ubalance = qq.balance
        u_pay = Payment.objects.filter(FK_User = user)
        for x in u_pay:
           my_savings += x.Amount_of_payment

    else:
        uname = 'Anonim' 
        return HttpResponseRedirect('/login/')
    return render_to_response('main.html',{'user':uname, 'balance':ubalance, 'count_user':count_user,  'my_savings' : my_savings})

