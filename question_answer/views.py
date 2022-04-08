from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.template.loader import render_to_string
from django.http import JsonResponse
from question_answer.models import ActiveQuestion, Answer
from question_answer.forms import AnswerCreateForm
from .forms import AnswerCreateForm, QuestionCreateForm, OptionCreateForm, ActiveQuestionCreateForm
from teacher.models import TimeTable
import json

User = get_user_model()


def create_question(request):
    user = request.user
    text = request.GET.get('text', 'Question not added')
    options = json.loads(request.GET.get('options', []))
    instance = QuestionCreateForm()
    question_id = instance.createQuestion(text=text, teacher=user)
    instance = OptionCreateForm()
    for option in options:
        instance.createOption(text=option, question_id=question_id)
    data = {
        'is_added': True,
    }
    return JsonResponse(data)


def active_question(request):
    user = request.user
    question_id = int(request.GET.get('question_id', 0))
    instance = ActiveQuestionCreateForm()
    instance.createActiveQuestion(question_id)
    data = {
        'is_added': True,
    }
    return JsonResponse(data)


def answer_question(request):
    user = request.user
    option_id = request.GET.get('option', 0)
    instance = AnswerCreateForm()
    instance.createAnswer(option_id=option_id, student=user)
    data = {
        'is_added': True,
    }
    return JsonResponse(data)


def answer_question(request):
    if request.is_ajax():
        user = request.user
        if user is None:
            return JsonResponse({})
        option_id = int(request.GET.get("option_id") or 0)
        if option_id != -1:
            instance = AnswerCreateForm()
            instance.createAnswer(option_id=option_id, student=user)
        answer_objs = Answer.objects.filter(student=request.user)
        active_qs = ActiveQuestion.objects.exclude(
            question__id__in=[answer.active_question.question.id for answer in answer_objs])
        if len(active_qs):
            active_qs = active_qs[0]
        else:
            active_qs = []
        tot_ans = len(answer_objs)
        tot_qs = len(ActiveQuestion.objects.all())

        data = render_to_string(
            template_name="student/partial_quiz.html",
            context={"active_qs": active_qs,
                     'tot_ans': tot_ans, 'tot_qs': tot_qs},
        )
        return JsonResponse(data, safe=False)


def create_timetable(request):
    name = request.GET.get('name', 'Subject Not Provided')
    time_duration = request.GET.get('time_duration', 'Not Provided')
    link = request.GET.get('link', 'Link Not Provided')
    instance = TimeTable(name=name, time_duration=time_duration, link=link)
    instance.save()
    data = {
        'is_added': True,
    }
    return JsonResponse(data)
