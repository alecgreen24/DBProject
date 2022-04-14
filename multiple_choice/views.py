from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .dao import connect 
from .daos.student_dao import *
from .daos.student import Student
from group_project.settings import *

SDAO = StudentDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])

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
            new_student = Student(username, password)
            response = SDAO.createStudent(new_student)
            if response == "success":
                request.session['username'] = new_student.username
                return HttpResponseRedirect(reverse("tests"))
            else:
                return render(request, "main.html", {
                    "message": response
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
        return render(request, "signup.html")


def tests(request):
    if not request.session.get('username'):
        print("NO STUDENT SESSION")
        return  HttpResponseRedirect(reverse("login"))
    return render(request, "quiz.html")
