from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def login(request):
    return render(request, "task/login.html")#the render for login

def register(request):
    if request.method == "POST":
        user_data = UserCreationForm(request.POST)
        if user_data.is_valid():
            user_data.save()
            return redirect("home:homeView")
        else:
            pass
    context = {
        "form": UserCreationForm()
    }
    return render(request, "task/django-register.html")