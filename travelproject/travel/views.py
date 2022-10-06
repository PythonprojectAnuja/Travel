from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from travel.models import place, team


def index(request):
    obj=place.objects.all()
    obj1=team.objects.all()
    return render(request,'index.html',{'result':obj,'team':obj1})