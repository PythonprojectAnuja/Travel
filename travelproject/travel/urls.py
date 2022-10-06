from django.shortcuts import render

from django.urls import path
from . import views

urlpatterns = [
   path('',views.index,name='index'),
    #path('aboutus/',views.about,name='about'),
    #path('contactus/',views.contact,name='contact'),
    #path('result/',views.result,name='result')
]