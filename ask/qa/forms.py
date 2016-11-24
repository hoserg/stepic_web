from django import forms
from django.forms import ModelForm
from models import Question, Answer

class AskForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ('title', 'text')
        
class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ('text', 'question')
