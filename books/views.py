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
import datetime

# Create your views here.

#Showing the index(register) page
def index(request):
    return render(request, "books/index.html")

#Checking if user is logged in
def checkloginstatus(request):
    if not request.user.is_authenticated:
        return render(request, "books/login.html")
    else:
        request.session['name'] = request.user.first_name
        context = {
            "user": request.user.first_name,
            "books": Book.objects.all().order_by('isbn')
        }
        return render(request, "books/account.html", context)

#Logging in user
def login_view(request):
    email = request.POST["email"]
    password = request.POST["password"]
    request.session['emailid'] = email
    print(request.session['emailid'])
    user = authenticate(request, email=email, password=password)
    if user is not None:
        login(request, user)
        return HttpResponseRedirect(reverse("checkloginstatus"))
    else:
        return render(request, "books/login.html", {"message": "Invalid credentials."})

#Logging out user
def logout_view(request):
    logout(request)
    return render(request, "books/index.html", {"message": "You are logged out."})

#Registering new users
def register(request):
    email = request.POST['email']
    password = request.POST['password']
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    is_admin = False
    CustomUser.objects.create_user(email=email, password=password, first_name = first_name, last_name = last_name, is_admin = is_admin)
    return render(request, "books/success.html", {"message":"YOU HAVE CREATED AN ACCOUNT"})

#Showing book details
def singlebook(request, id):
    book = Book.objects.get(pk = id)
    book_id = id
    book_title = book.title
    book_isbn = book.isbn
    book_author = book.author
    book_year = book.year
    numberoftimes = BorrowedBooks.objects.filter(id_book = id).count()
    context = {
        "id": book_id,
        "title": book_title,
        "isbn": book_isbn,
        "author": book_author,
        "year": book_year,
        "numberoftimes": numberoftimes
    }
    return render(request, "books/singlebook.html", context)

def borrow(request, id):
    email = request.session['emailid']
    #Checking if users have returned the previous books(if any)
    oldbooks = BorrowedBooks.objects.filter(member_email = email)
    numberofoldbooks = oldbooks.count()
    if numberofoldbooks == 3:
        for i in range(3):
            book = Books.objects.all()[i]
            returndate = book.returndate
            currentdate = datetime.datetime.now()
            if returndate < currentdate:
                return render(request, "books/error.html")
            else:
                pass
    else:   
        Borrowed.objects.create(id_book = id, member_email = email, dateofborrowing = datetime.datetime.now, returndate = datetime.datetime.now + datetime.timedelta(days = 7))
        return render(request, "books/success.html")