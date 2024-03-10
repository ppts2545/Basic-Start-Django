from django.shortcuts import render
from django.http import HttpRequest

def say_hello(request):
    
    return render(request, 'hello.html')

def page1Render(request):
    """Renders the 'page1.html' template without any dynamic content."""
    return render(request, 'page1.html')

def pageFormRender(request):
    """Renders the 'form.html' template without any dynamic content."""
    return render(request, 'form.html')