from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

#class QuestionManager(models.Manager):
#    def new(self):
#        return self.objects.all().order_by('-added_at')
#    def popular(self):
#        return self.objects.all().order_by('-rating')

class Question(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User, default=1)  
    likes = models.ManyToManyField(User, related_name='question_like_user')
    
    #qobjects = models.Manager()
    #objects = QuestionManager()

    def __unicode__(self):
        return self.title
    
    def get_url(self):
        return reverse('question', kwargs={'id': self.id})

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  
    author = models.ForeignKey(User, default=1)

    def get_url(self):
        return self.question.get_url()    
