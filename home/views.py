from django.shortcuts import render

# Create your views here.
#This is a function based view


def home(request):
    return render(request, "home/index.html")

def about(request):
    return render(request, "home/about.html")

def contact(request):
    return render(request, "home/contact.html")

def services(request):
    return render(request, "home/services.html")
