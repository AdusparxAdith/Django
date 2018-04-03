from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
    return render(request, "core/index.html")

def forum(request):
    return render(request, "core/forum.html")

def signin(request):
    return render(request, "core/login.html")

def signup(request):
    return render(request, "core/signup.html")

def signout(request):
    logout(request)
    return redirect("/")
