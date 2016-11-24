from django.template import loader, Context, RequestContext
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import Question, User
from forms import AskForm, AnswerForm

def proba(request):
    return HttpResponse('OK')

def question(request, qid):
    #if request.method is 'POST':
        #return answer(request)
        #return HttpResponse('OK')
    question = get_object_or_404(Question, id=qid)
    answer = AnswerForm({"question": question.id})
    return render(request, 'question.html', {
        'question': question,
        'answers': question.answer_set.all(),
        'form': answer
        })

def newqa(request):
    qmain = Question.objects.all().order_by('-id')
    
    paginator = Paginator(qmain, 10)
    page = request.GET.get('page')
    try:
        qmain = paginator.page(page)
    except PageNotAnInteger:
        qmain = paginator.page(1)
    except EmptyPage:
        qmain = paginator.page(paginator.num_pages)
    
    t = loader.get_template("new.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))

def popular(request):
    qmain = Question.objects.all().order_by('-rating')
    
    paginator = Paginator(qmain, 10)
    page = request.GET.get('page')
    try:
        qmain = paginator.page(page)
    except PageNotAnInteger:
        qmain = paginator.page(1)
    except EmptyPage:
        qmain = paginator.page(paginator.num_pages)
    
    t = loader.get_template("popular.html")
    c = Context({'questions':qmain, 'request':request})
    return HttpResponse(t.render(c))
   
def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            #question.author = request.user
            #question.save()
            #url = question.get_url()
            return HttpResponseRedirect(reverse('question', args=[question.id,])  
    else:
        form = AskForm()
        t = loader.get_template("askform.html")
        c = RequestContext(request, {'form':form})
        return HttpResponse(t.render(c))
        
def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            answer.author = request.user
            answer.save()
            return HttpResponseRedirect(answer.get_url())        
    else:
        form = AnswerForm()
        t = loader.get_template("answerform.html")
        c = RequestContext(request, {'form':form})
        return HttpResponse(t.render(c))
    
        
