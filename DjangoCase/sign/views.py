from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def index(request):
    return render(request,"index.html")

def login_action(request):
    if request.method == 'POST':
        username = request.POST.get('Username','')
        password = request.POST.get('Password','')
        if username=='admin' and password == 'admin123':
            return HttpResponse('Login Success!')
        else:
            return render(request,'index.html',{'error':'username or password error!'})

