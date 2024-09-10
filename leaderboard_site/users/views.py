from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import loader
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile

def login(request):
    if 'fail' in request.COOKIES:
        return TemplateResponse(request, 'login.html', {"error":"Invalid username or password"})
    else:
        return TemplateResponse(request, 'login.html', {})

def register(request):
    return TemplateResponse(request, 'register.html', {})


@csrf_protect
def login_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        
        user = None
        request = None
              
        try:
            user = UserProfile.objects.get(uname=uname)
            check = check_password(pword, user.pword_hash)
            
            del pword
            
            if check:
                
                return HttpResponse("Home page redirect")
            else:
                response = HttpResponseRedirect("/member/")
                response.set_cookie("fail")
                return response
        except:
            response = HttpResponseRedirect("/member/")
            response.set_cookie("fail")
            return response
            
    return HttpResponse("Unexpected error")


@csrf_protect
def registration_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        
        if request.POST.get('password') != request.POST.get('reenter'):
            del request
            return HttpResponse("Re entered password incorrect")
        
        del request
        
    
        
        
        UserProfile.objects.create(
            uname = uname,
            pword_hash = pword,
            email = email
        )
        
        return HttpResponse("Success")
    return HttpResponse("Fail")
