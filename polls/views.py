from django.http import HttpResponse
from django.shortcuts import render
from .models import Question, Reader
from .mixin import get_obj_or_404


def index(request):
    latest_question_list = Question.objects.order_by('-pud_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_obj_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def comments(request, reader_id):
    reader = get_obj_or_404(Reader, pk=reader_id)
    return render(request, 'polls/reader.html', {'reader': reader})

def results(request, reader_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % reader_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)


