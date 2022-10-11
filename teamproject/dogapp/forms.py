from django import forms
from dogapp.models import Question

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제 목',
            'content': '내 용',
        }