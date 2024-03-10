from django.shortcuts import render
from django.http import HttpRequest
from playground.models import Person

def say_hello(request):
    all_person = Person.objects.all()
    return render(request, 'hello.html', {"all_person":all_person})

def page1Render(request):
    """Renders the 'page1.html' template without any dynamic content."""
    return render(request, 'page1.html')

def pageFormRender(request):
    """Renders the 'form.html' template without any dynamic content."""
    return render(request, 'form.html')