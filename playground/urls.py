from django.urls import path
from . import views  # Assuming you have a 'views.py' file in your 'playground' app

urlpatterns = [
    path('', views.say_hello, name='playground_hello'),  # Name the URL pattern for future reference
    path('about/', views.page1Render, name='playground_page1Render'),
    path('form/', views.pageFormRender, name='formpage_render')
]