from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import *
import random
from django.http import HttpResponseForbidden
from django.db import IntegrityError
from .models import CustomUser
from .managers import CustomUserManager

# Create your views here.

"""Showing the homepage"""
def index(request):
    return render(request, "books/index.html")

def checkloginstatus(request):
    if not request.user.is_authenticated:
        return render(request, "books/login.html")
    else:
        request.session['name'] = request.user.first_name
        context = {
            "user": request.user.first_name
        }
        return render(request, "books/account.html", context)

def login_view(request):
    email = request.POST["email"]
    password = request.POST["password"]
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("checkloginstatus"))
    else:
        return render(request, "books/login.html", {"message": "Invalid credentials."})

def logout_view(request):
    logout(request)
    return render(request, "books/index.html", {"message": "Logged out."})

def register(request):
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    is_admin = False
    CustomUser.objects.create_user(email=email, password=password, first_name = first_name, last_name = last_name, is_admin = is_admin)
    return render(request, "books/success.html", {"message":"YOU HAVE CREATED AN ACCOUNT"})
    