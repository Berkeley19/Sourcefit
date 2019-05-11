from django.shortcuts import render
from django.http import HttpResponse

def login(request):
    return HttpResponse('<h1>Login</h1>')

def register(request):
    return HttpResponse('<h1>Register</h1>')