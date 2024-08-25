from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.contrib.auth.hashers import make_password

def login(request):
    return TemplateResponse(request, 'login.html', {})

def register(request):
    return HttpResponse(request, 'register.html', {})

@csrf_protect
def login_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = make_password(request.POST.get('password'))
        
        request=None

@csrf_protect
def registration_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = make_password(request.POST.get('password'))
        email = request.POST.get('email')
        
        request=None
