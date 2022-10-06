from django.contrib import messages, auth
from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        user = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']
        if pass1 == pass2:
            if (User.objects.filter(username=user).exists()):
                return HttpResponse('User name already exist')
            if (User.objects.filter(email=email).exists()):
                return HttpResponse("Email already exist")
            else:
                model = User.objects.create_user(user, email, pass1)
                model.save()
                return render(request, 'index.html')
        else:
            return HttpResponse('password mismatch')

    else:

        return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        user = request.POST['username']
        pass1 = request.POST['password1']
        print(user)
        print(pass1)
        us = authenticate(username=user, password=pass1)
        print(us)
        if us is not None:
            # login(request,us)
            return render(request,'index.html')

        else:
            return HttpResponse('Password Mismatch')
    else:
        return render(request,'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')