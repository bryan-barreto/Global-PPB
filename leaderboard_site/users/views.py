from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotAllowed
from django.template import loader
from django.template.response import TemplateResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt

def login(request):
    return TemplateResponse(request, 'login.html', {})

def register(request):
    html_page = loader.get_template('register.html')
    return HttpResponse(html_page.render())

@csrf_protect
def login_handler(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pword = request.POST.get('password')

        # Process the data (e.g., save to database, send an email, etc.)

        return HttpResponse(f"Received POST request. Name: {uname}, Email: {pword}")
    else:
        return HttpResponseNotAllowed(['POST'])