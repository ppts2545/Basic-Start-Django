from django.shortcuts import render

def say_hello(request):
    """Renders the 'hello.html' template with dynamic content."""
    context = {'name': 'Poom', 'age': 21}  # Combine name and age into one dictionary
    return render(request, 'hello.html', context)

def page1Render(request):
    """Renders the 'page1.html' template without any dynamic content."""
    return render(request, 'page1.html')

def pageFormRender(request):
    """Renders the 'form.html' template without any dynamic content."""
    return render(request, 'form.html')