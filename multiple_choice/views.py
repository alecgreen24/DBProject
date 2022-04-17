from django.shortcuts import render
from django.http import HttpResponse
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

def list(request):
    if not request.session.get('username'):
        print("NO STUDENT SESSION")
        return  HttpResponseRedirect(reverse("login"))
    return render(request, "list.html")



def index(request):
    if request.session.get('username'):
        return HttpResponseRedirect(reverse("list"))
    else:
        return HttpResponseRedirect(reverse("login"))

def addquestions(request):
    return render(request, "add_questions.html")


def login(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        if not username:
            return render(request, "login.html", {
                "message": "Username is empty."
            })
        elif not(password):
            return render(request, "login.html", {
                "message": "Password can't be empty."
            })
        logged_student = Student(username, password)
        id =  SDAO.checkCredentials(logged_student)
        if id:
            request.session['username'] = logged_student.username
            return HttpResponseRedirect(reverse("list"))

        return render(request, 'login.html', {
            "message": "Wrong username or/and passsword."})
    return render(request, 'login.html')



def signup(request):
    # Register user
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirmation = request.POST.get("confirmation")
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
        new_student = Student(username, password)
        response = SDAO.createStudent(new_student)
        if response == "success":
            request.session['username'] = new_student.username
            return HttpResponseRedirect(reverse("menu"))
        else:
            return render(request, "signup.html", {
                "message": response
            })
    else:
        return render(request, "add_test.html")


def new(request):
    return render(request, "new_test.html")

def edit(request):
    return render(request, "edit_test.html")

def account(request):
    return render(request, "account_info.html")

def take_test(request):
    return render(request, "take_test.html")
        

def logout(request):
    if request.session.get('username'):
        del request.session['username']
    return HttpResponseRedirect(reverse("login"))
