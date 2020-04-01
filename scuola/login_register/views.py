from django.shortcuts import render
from .models import Register
from django.core.mail import EmailMessage, send_mass_mail
from email_validator import validate_email, EmailNotValidError
from django.http import JsonResponse
import json
import re


def login(request):
    return render(request, 'login.temp.html')


def req_register(request):
    return render(request, 'register.temp.html')


def register(request):
    name = request.GET.get('name')
    surname = request.GET.get('surname')
    email = request.GET.get('email')
    password = request.GET.get('pwd')
    password2 = request.GET.get('pwd2')

    succ = {'success': "You've registered successfully"}
    
    valName = 1 if name is not "" else 0
    valSurname = 1 if surname is not "" else 0

    try:
        v = validate_email(email)
        mail = v["email"]
        if Register.objects.filter(email = mail):
            mail = 0
        else:
            mail = v["email"]

    except EmailNotValidError as e:
        mail = 0
    pwd = validatePassword(password, password2)

    if (mail is not 0) and (pwd is not 0):  
        reg = Register(name=name, surname=surname, email=email, password=password)
        reg.save();
        return JsonResponse(succ)
    
    msg = {'name': valName, 'surname': valSurname, 'mail': mail, 'password': pwd, 'success': 0}

    return JsonResponse(msg)

def validatePassword(pwd1, pwd2):
    if (pwd1 == pwd2) and pwd1 is not "":
        return 1
    else:
        return 0
