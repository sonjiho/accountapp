from django.shortcuts import render, get_object_or_404, redirect
from .models import Question
from django.utils import timezone
from .forms import QuestionForm

def index(request):
    """ 목록 출력"""
    question_list = Question.objects.order_by('-create_date')
    context={'question_list':question_list}
    return render(request, 'dogapp/question_list.html', context)

def detail(request, question_id):
    """질문 내용 출력"""
    question=get_object_or_404(Question, pk=question_id)
    context={'question':question}
    return render(request, 'dogapp/question_detail.html', context)

def answer_create(request, question_id):
    """답변 등록"""
    question=get_object_or_404(Question,pk=question_id)
    question.answer_set.create(content=request.POST.get('content'), create_date=timezone.now())
    return redirect('dogapp:detail', question_id=question.id)

def question_create(request):
    """질문 등록"""
    if request.method == 'POST' :
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.create_date = timezone.now()
            question.save()
            return redirect('dogapp:index')
    else:
        form = QuestionForm()
    context = {'form':form}
    return render(request, 'dogapp/question_form.html', context)