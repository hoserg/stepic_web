from django.shortcuts import render
from django.http import HttpRequest

def test(request, *args, **kwargs):
    return HttpResponse('OK')
