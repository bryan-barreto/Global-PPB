from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed, HttpResponseRedirect
from django.template import loader
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password, check_password
from .models import UserProfile

def login(request):
    errors = {}
    if 'error' in request.COOKIES:
        errors['error'] = "Invalid username or password"
    response = TemplateResponse(request, 'login.html', errors)
    for error in errors:
        response.delete_cookie(error)
    return response

def register(request):
    errors = {}
    if 'uerror' in request.COOKIES:
        errors['uerror'] = "Username already exists"
    if 'ulerror' in request.COOKIES:
        errors['uerror'] = "Username must be a minimum of 6 characters"
    if 'perror' in request.COOKIES:
        errors['perror'] = "Passwords do not match"
    if 'plerror' in request.COOKIES:
        errors['perror'] = "Password must be a minimum of 8 characters"
    response = TemplateResponse(request, 'register.html', errors)
    for error in request.COOKIES:
        response.delete_cookie(error)
    return response


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
                response.set_cookie("error")
                return response
        except:
            response = HttpResponseRedirect("/member/")
            response.set_cookie("error")
            return response
            
    return HttpResponse("Unexpected error")


@csrf_protect
def registration_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        
        response = HttpResponseRedirect("/member/register")
    
        
        try:
            if len(uname) < 6:
                response.set_cookie("ulerror")
            elif len(UserProfile.objects.get(uname=uname)):
                response.set_cookie("uerror")
        except:
            pass

        if len(request.POST.get('password')) < 8:
            response.set_cookie("plerror")
        elif request.POST.get('password') != request.POST.get('reenter'):
            response.set_cookie("perror")
            
        del request
        
        if len(response.cookies) > 0:
            return response
        
        
        UserProfile.objects.create(
            uname = uname,
            pword_hash = pword,
            email = email
        )
        
        return HttpResponse("Home page redirect")
    return HttpResponse("Unexpected error")
