
from django.contrib import admin
from django.urls import path
from app01 import views

urlpatterns = [
   
    #  http://127.0.0.1:8000/login/  ->  login
    path('login/', views.login),
   


  
]
