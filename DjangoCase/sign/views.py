from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('Username','')
        password = request.POST.get('Password','')
        if username=='admin' and password == 'admin123':
            response =  HttpResponseRedirect('/login_seccess/')
            request.session['user'] = username
            return response
        else:
            return render(request,'index.html',{'error':'username or password error!'})

def login_seccess(request):
    username = request.session.get('user','')
    return render(request,'login_seccess.html',{'user':username})

