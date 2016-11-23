from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse
from .models import *

def question(request, qid):
    #qmain = Question.objects.get(id=qid)
    #qanswer = Answer.objects.filter(question__id=qid)
    #t = loader.get_template("question.html")
    #c = Context({'question':qmain, 'answers':qanswer, 'request':request})
    #return HttpResponse(t.render(c))
    return HttpResponse('QQQ')

def newqa(request):
    #qmain = Question.objects.all().order_by('-id')
    #t = loader.get_template("new.html")
    #c = Context({'questions':qmain, 'request':request})
    #return HttpResponse(t.render(c))
    return HttpResponse('QQQ')

def popular(request):
    #qmain = Question.objects.all().order_by('-rating')
    #t = loader.get_template("popular.html")
    #c = Context({'questions':qmain, 'request':request})
    #return HttpResponse(t.render(c))
    return HttpResponse('QQQ')
