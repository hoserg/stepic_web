from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def question(request, *args, **kwargs):
    return HttpResponse('OK')
