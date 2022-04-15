from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .dao import connect
from .daos.student import *



# Create your views here.
def index(request):
    return HttpResponseRedirect(reverse("signup"))


def login(request):
    return render(request, 'login.html')


def signup(request):
    # Register user
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if not username:
            return render(request, "signup.html", {
                "message": "Username is empty."
            })
        elif not(password):
            return render(request, "signup.html", {
                "message": "Password can't be empty."
            })
        if password != confirmation:
            return render(request, "signup.html", {
                "message": "Passwords must match."
            })
        else:
            createStudent(username, password)
            return render(request, "signup.html", {
                "message": "Success creating the student."
            })
        # Attempt to create new user
        # try:
        #     connect('INSERT INTO student {username} ')
        # except IntegrityError:
        #     return render(request, "capstone/register.html", {
        #         "message": "Username already taken."
        #     })
        # login(request, user)
        # return HttpResponseRedirect(reverse("user_extra_info"))
    else:
        return render(request, "newTest.html")
