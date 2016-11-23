from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from qa.models import Question

def proba(request):
    return HttpResponse('OK')

def newqa(request):
    qmain = Question.objects.all().order_by('-id')
    t = loader.get_template("new.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))

def popular(request):
    qmain = Question.objects.all().order_by('-rating')
    t = loader.get_template("popular.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
