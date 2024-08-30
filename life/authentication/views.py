from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest
from django.contrib.auth import authenticate, login, logout
# Create your views here.
from .forms import CreateUserForm

def registration(request):
    form = CreateUserForm()
    context = {'form': form}

    if(request.method == 'POST'):
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/auth/login")
    return render(request,'auth/sign.html', context)

def loginPage(request:HttpRequest):
    context = {}
    username =''
    password=''
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(request.POST.get('username'))
    user = authenticate(request, username=username,password=password)
    print(user)
    if(user is not None):
        login(request,user)
        return redirect('/auth/login')

    return render(request,'auth/login.html', context)

def logoutPage(request):
    logout(request)
    return redirect("/auth/login")

def redirectTest(request:HttpRequest):
    return redirect("/auth/signup")

def SuperTest(request:HttpRequest):
    context = {}
    if(request.user.is_authenticated):
        return render(request,'core/navbar.html', context)
    return render(request,'core/navbar.html', context)