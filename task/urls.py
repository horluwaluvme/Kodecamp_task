from django.urls import path
from .views import login, register

#The urls of each link/page
app_name = "task"
   
urlpatterns = [
    path("login/", login, name = "loginView"),
    path('register/', register, name = "registerView")

]