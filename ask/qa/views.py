from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

def question(request, qid):
    qmain = Question.objects.get(id=qid)
    qanswer = Answer.objects.filter(question__id=qid)
    t = loader.get_template("question.htm")
    c = Context({'question':qmain, 'answer':qanswer, 'request':request})
    return HttpResponse(t.render(c))
