
from asyncio import QueueEmpty
import json
from django.core.serializers.json import DjangoJSONEncoder
from group_project.settings import *
from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from .daos.student_dao import *
from .daos.student import Student
from .daos.test_dao import *
from .daos.test import Test
from .daos.answer_dao import *
from .daos.answer import Answer
from .daos.question_dao import *
from .daos.question import Question
from .daos.question_answer_dao import *
from .daos.question_answer import QuestionAnswer
from .daos.test_question_dao import *
from .daos.test_question import TestQuestion


SDAO = StudentDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
TDAO = TestDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
ADAO = AnswerDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
QDAO = QuestionDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
QADAO = QuestionAnswerDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])
TQDAO = TestQuestionDAO(host=DATABASES['default']['HOST'],
                database=DATABASES['default']['NAME'],
                user=DATABASES['default']['USER'],
                password=DATABASES['default']['PASSWORD'])


def isAuthenticated(request):
    if request.session.get('id'):
        return True
    return render(request, "login.html", {
        "message": "You must log in to access all functionalities."
    })

def storeQuestions(questions, test_id):
    questions = np.array(questions)
    questions_ids = []
    for question_set in questions:
        question_set = [str(i) for i in question_set.split(',')]
        question_content = question_set[0]
        answers = question_set[1:-1]
        answers_ids = []
        correct_answer_id = None
        correct_answer = question_set[4].lower()
        for answer_content in answers:
            answer = Answer(answer_content)
            answers_ids.append(ADAO.createAnswer(answer))
        if correct_answer != 'a' and correct_answer != 'b' and correct_answer != 'c':
            print("No correct answer!")
            raise Exception
        if correct_answer == 'a':
            correct_answer_id = answers_ids[0]
        elif correct_answer == 'b':
            correct_answer_id = answers_ids[1]
        else:
            correct_answer_id = answers_ids[2]
        question = Question(content = question_content, correct_answer_id = correct_answer_id)
        q_id = QDAO.createQuestion(question)
        for answer_id in answers_ids:
            qa = QuestionAnswer(q_id, answer_id)
            QADAO.createQuestionAnswer(qa)
        questions_ids.append(q_id)
    for question_id in questions_ids:
        tq = TestQuestion(test_id, question_id)
        TQDAO.createTestQuestion(tq)
    return True
    

def list(request):
    if isAuthenticated(request):
        tests = TDAO.getAllTests()
        return render(request, "list.html", {"tests": tests})



def index(request):
    if isAuthenticated(request):
        return HttpResponseRedirect(reverse("list"))
    

def add_questions(request):
    if isAuthenticated(request):
        if request.method == 'POST':
            questions = request.POST.getlist('questions[]')
            test_id = request.POST.get('test_id')
            if storeQuestions(questions, test_id):
                return HttpResponseRedirect(reverse("list"))
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
            new_test = Test(creator_id = creator_id, title = title)
            id = TDAO.createTest(new_test)
            new_test.id = id  
            if isinstance(id, int):
                return render(request, "add_questions.html", {"new_test": new_test})
            return render(request, "new_test.html", {
                    "message": "There was an error creating the test."})
        return render(request, "new_test.html")

def possible_tests(request):
    if isAuthenticated(request):
        tests = TDAO.getAllTests()
        return render(request, "possible_tests.html", {"tests": tests})
   
def take_test(request, test_id):
    test = TDAO.getOneTest(test_id)
    questions = TDAO.getQuestions(test)
    return render(request, "test_page1.html", {
    'test': test,
    'questions': questions,
    })


def test_taken(request, test_id):
    if request.method == "POST":
        test = TDAO.getOneTest(test_id)
        questions = TDAO.getQuestionsAndAnswer(test)

def edit(request):
    if isAuthenticated(request):
        tests = TDAO.getAllTests()
        return render(request, "edit_test.html", {"tests": tests})

def editor(request, test_id):
    test = TDAO.getOneTest(test_id)
    questions = TDAO.getQuestions(test)
    if request.method == "POST":
        for question in questions:
            question_id = request.POST.get(f"{question.id}")
            id = QDAO.deleteQuestion(question)
            id = QDAO.createQuestion(question)
    return render(request, 'editor.html', {"test_id":test_id, "questions": questions})

def account(request):
    return render(request, "account_info.html")


def logout(request):
    if request.session.get('id'):
        del request.session['id']
    return HttpResponseRedirect(reverse("login"))

def tests_taken(request):
    if isAuthenticated(request):
        tests = TDAO.getAllTests()
        return render(request, "tests_taken.html", {"tests": tests})