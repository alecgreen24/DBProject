from django.shortcuts import render
from django.http import HttpResponse
from .dao import connect



# Create your views here.
def index(request):
    connect()
    return render(request, 'login.html')
