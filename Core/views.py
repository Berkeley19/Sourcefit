from django.shortcuts import render
from django.http import HttpResponse

def core(request):
    return HttpResponse('<h1>Core</h1>')
