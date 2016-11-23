from django.db import models
from django.contrib.auth.models import User

class Question(models.Model):
    title = models.CharField(max_length=64)
    text = models.TextField()
    added_at = models.DateField(auto_now=False, auto_now_add=False)
    rating = models.IntegerField()
    author = models.ForeignKey(User)  
    likes = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title

class Answer(models.Model):
    text = models.CharField(max_length=255)
    added_at = models.DateField(auto_now=False, auto_now_add=False)
    question = models.ForeignKey(Question)  
    author = models.ForeignKey(User)
