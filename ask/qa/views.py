from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, get_object_or_404
from models import Question, User

def proba(request):
    return HttpResponse('OK')

def question(request, qid):
    question = get_object_or_404(Question, id=id)
    return render(request, 'question.html', {
        'question': question,
        'answers': question.answer_set.all()
        })

def newqa(request):
    qmain = Question.objects.all().order_by('-id')
    t = loader.get_template("new.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
    #return HttpResponse('QQQ')

def popular(request):
    qmain = Question.objects.all().order_by('-rating')
    t = loader.get_template("popular.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
    #return HttpResponse('QQQ')
