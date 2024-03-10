from django.shortcuts import render,redirect
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
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST["name"]
        age = request.POST["age"]
        print(name ,age)
        return redirect("/")
        #บันทึกข้อมูล
     
    else :
        return render(request, 'form.html')
  