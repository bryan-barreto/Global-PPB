from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    html_page = """
    <link rel="stylesheet" href="css/cite.css">
    <html>
        <div class="login_page">
            <h2>Login</h2>
            
        </div>
    </html>
    """
    return HttpResponse(html_page)
    