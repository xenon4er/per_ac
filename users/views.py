from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from per_ac.users.models import *
from per_ac.views import *

from django.template import RequestContext
from django.core.context_processors import csrf

from django.views.decorators.csrf import csrf_protect

from django.views.generic.simple import direct_to_template
from forms import *



@csrf_protect
def registr(request):
    count_user = User.objects.count()
    my_savings = GetMySavings(request.user);
    lastUserJoined = GetLastJoined()
    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')
  
    errors_registr = []
    
    form = RegAddform(request.POST or None)
    context = { 'form': form,  'errors':errors_registr, 'count_user':count_user,  'my_savings' : my_savings}
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        email = form.cleaned_data.get('email',  None)
        
        user = form.SaveUser(username, email, password)
        return HttpResponseRedirect('/login/')
        
    return direct_to_template(request, 'regist.html',  context)
     

@csrf_protect    
def login(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/welcome/')
    count_user = User.objects.count()
    errors_login = []
    form = LoginAddform(request.POST or None)
    lastUserJoined = GetLastJoined()
    context = { 'form': form,  'errors':errors_login, 'count_user':count_user}

    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username', None)
        password = form.cleaned_data.get('password', None)
        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect('/welcome/')
        else:
            errors_login.append("User not found")
    return direct_to_template(request, 'login.html', context)
    

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
    return HttpResponseRedirect('/welcome/')    

@csrf_protect
def edit_user_profile(request):
    user = request.user
    lastUserJoined = GetLastJoined()
    count_user = User.objects.count()
    if not user.is_authenticated():
        return HttpResponseRedirect('/welcome/') 
    
    my_savings = GetMySavings(user)
    
    errors_login = []    
    data = {'firstname': user.first_name, 'lastname': user.last_name, 'email': user.email, 'password': user.password}    
    form = EditUserForm(request.POST or data)
    
    context = { 'form': form,  'errors':errors_login, 'count_user':count_user,  'my_savings' : my_savings}
    if request.method == 'POST' and form.is_valid():
        firstname = form.cleaned_data.get('firstname', None)
        lastname = form.cleaned_data.get('lastname', None)
        password = form.cleaned_data.get('password', None)
        email = form.cleaned_data.get('email',  None)
        
        form.SaveChanges(user, firstname, lastname, email, password)
        return HttpResponseRedirect('/welcome/')
    
    return direct_to_template(request, 'edit_profile.html', context)
