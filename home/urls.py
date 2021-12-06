# from typing import Pattern
from django import urls
from django.urls import path
# from django.views.generic.base import TemplateView
# from django.views.generic.base import ListView
from . import views

app_name = 'home'

urlpatterns = [
         path('', views.blog_home, name='blog_home'),      
]