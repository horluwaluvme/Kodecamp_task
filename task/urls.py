from django.urls import path
from .views import home, about, login

#The urls of each link/page
#    
urlpatterns = [
    path("home", home),
    path('about/', about),
    path('login/', login),
]