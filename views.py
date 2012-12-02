from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect

def welcome(request):
    user = request.user
    count_user = User.objects.count()
    return render_to_response('welcome.html',{'user':user, 'count_user':count_user})

def main_menu(request):
    count_user = User.objects.count()
    if request.user.is_authenticated():
        uname = request.user.username
        #ubalance = "dsf"#request.user.balance
        qq = request.user.get_profile()
        ubalance = qq.balance
    else:
        uname = 'Anonim' 
        return HttpResponseRedirect('/login/')
    return render_to_response('main.html',{'user':uname, 'balance':ubalance, 'count_user':count_user})

