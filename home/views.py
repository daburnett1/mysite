from django.views.generic import ListView
from django.shortcuts import render

def blog_home(request):
    # return response
    return render(request, "home/index.html")