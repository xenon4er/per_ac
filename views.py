from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from per_ac.accounts_department.models import *
from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect

def GetMySavings(user):
    my_savings = 0.0
    if user.is_authenticated():
        u_pay = Payment.objects.filter(FK_User = user)
        for x in u_pay:
            my_savings += x.Amount_of_payment
    return my_savings

def GetLastJoined():
    userlist = User.objects.order_by('-date_joined')
    userlast = userlist[0]
    return userlast
    
    
def welcome(request):
    user = request.user
    count_user = User.objects.count()
    my_savings = GetMySavings(user)
    lastUserJoined = GetLastJoined()
    return render_to_response('welcome.html',{'user':user,'lastuser':lastUserJoined, 'count_user':count_user, 'my_savings' : my_savings})

def main_menu(request):
    user = request.user
    count_user = User.objects.count()
    my_savings = GetMySavings(user)
    lastUserJoined = GetLastJoined()
    
    if user.is_authenticated():
        uname = user.username
        #ubalance = "dsf"#request.user.balance
        qq = user.get_profile()
        ubalance = qq.balance
        
    else:
        uname = 'Anonim' 
        return HttpResponseRedirect('/login/')
    return render_to_response('main.html',{'user':uname,'lastuser':lastUserJoined, 'balance':ubalance, 'count_user':count_user,  'my_savings' : my_savings})

