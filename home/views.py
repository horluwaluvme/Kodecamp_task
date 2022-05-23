from django.shortcuts import render

# Create your views here.
#This is a function based view

from django.http import HttpResponse

def home (request):
    return HttpResponse ("<h1> User Homepage <h1/>")

def about (request):
    return HttpResponse ("<h1> About this page <h1/>")

def contact (request):
    return HttpResponse ('<h2> Contact <h2/>')

