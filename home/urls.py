from django.urls import path
from .views import home, about, contact

#The urls of each link/page
#    
urlpatterns = [
    path("", home),
    path("about/", about),
    path('contact/', contact)

]