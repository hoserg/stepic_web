from django.contrib.auth.models import User
from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateField(auto_now_add=True)
    rating = models.IntegerField(default = 0)
    author = models.ForeignKey(User)  
    likes = models.ManyToManyField(User, related_name='question_like_user')

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateField(auto_now_add=True)
    question = models.ForeignKey(Question, related_name='answer_question')  
    author = models.ForeignKey(User, related_name='answer_user')
