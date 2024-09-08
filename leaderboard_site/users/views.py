from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile

def login(request):
    return TemplateResponse(request, 'login.html', {})

def register(request):
    return TemplateResponse(request, 'register.html', {})

@csrf_protect
def login_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        
        user = None
        
        del request
        
        try:
            user = UserProfile.objects.get(uname=uname)
            if check_password(pword, user.pword_hash):
                del pword
                return HttpResponse("Success")
            else:
                return HttpResponse("Incorrect Username or Password") 
        except:
            return HttpResponse("Incorrect Username or Password")
            
    return HttpResponse("Fail")

@csrf_protect
def registration_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        
        del request
        
        
        UserProfile.objects.create(
            uname = uname,
            pword_hash = pword,
            email = email
        )
        
        return HttpResponse("Success")
    return HttpResponse("Fail")
