from django.shortcuts import render,redirect
from django.http import HttpRequest
from playground.models import Person

def say_hello(request):
    all_person = Person.objects.all()
    return render(request, 'hello.html', {"all_person":all_person})

def page1Render(request):
    return render(request, 'page1.html')


def pageFormRender(request):
    
    if request.method == "POST":
        #รับข้อมูล
        name = request.POST['name']
        age = request.POST['age']
        print(name , age)
        #บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            age = age
        )
        person.save()
        #เปลี่ยนเส้นทาง
        return redirect("/")
     
    else :
        return render(request, 'form.html')
  