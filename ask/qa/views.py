from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def test(request, *args, **kwargs):
    return HttpResponse('OK')
