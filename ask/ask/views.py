from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def proba(request):
    return HttpResponse('OK')

def newqa(request):
    qmain = Question.objects.all()
    t = loader.get_template("new.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
