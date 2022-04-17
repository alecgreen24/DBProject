from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.urls import reverse
from django.http import HttpResponse, HttpResponseRedirect
from .dao import connect 
from .daos.student_dao import *
from .daos.student import Student
from .daos.test_dao import *
from .daos.test import Test
from group_project.settings import *

SDAO = StudentDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
TDAO = TestDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])


def isAuthenticated(request):
    if request.session.get('id'):
        return True
    return render(request, "login.html", {
        "message": "You must log in to access all functionalities."
    })


def list(request):
    if isAuthenticated(request):
        return render(request, "list.html")



def index(request):
    if isAuthenticated(request):
        return HttpResponseRedirect(reverse("list"))
    

def addquestions(request):
    if isAuthenticated(request):
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
            logged_student.id = id
            request.session['id'] = logged_student.id
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
        id = SDAO.createStudent(new_student)
        if isinstance(id, int):
            new_student.id = id
            request.session['id'] = new_student.id
            return HttpResponseRedirect(reverse("list"))
        error_message = id
        return render(request, "signup.html", {
            "message": error_message
        })
    else:
        return render(request, "signup.html")

def new_test(request):
    if isAuthenticated(request):
        if request.method == "POST":
            title = request.POST.get("title")
            creator_id = request.session.get('id')
            new_test = Test(creator_id, title)
            id = TDAO.createTest(new_test)     
            if isinstance(id, int):
                return render(request, "add_questions.html", {"new_test": new_test})
            return render(request, "new_test.html", {
                    "message": "There was an error creating the test."})
        return render(request, "new_test.html")
        

def edit(request):
    return render(request, "edit_test.html")

def account(request):
    return render(request, "account_info.html")

def take_test(request):
    return render(request, "take_test.html")

def logout(request):
    if request.session.get('id'):
        del request.session['id']
    return HttpResponseRedirect(reverse("login"))
