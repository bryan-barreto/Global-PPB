from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def login(request):
    html_page = loader.get_template('login.html')
    return HttpResponse(html_page.render())
    