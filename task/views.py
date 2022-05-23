from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, "task/index.html")#the render file for home

def about(request):
    return render(request, "task/about.html")#the render for about

def login(request):
    return render(request, "task/login.html")#the render for login

