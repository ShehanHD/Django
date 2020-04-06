from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request, 'index.html')


def register(request):
    return render(request, 'register.html')


def login(request):
    return render(request, 'login.html')


def createUser(request):
    if request == 'createUser':
        #return HttpResponse("Here's the text of the Web page.")
        return render(request, 'login.html')