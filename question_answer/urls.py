from django.urls import path
from .views import create_question, active_question, answer_question, create_timetable
from .apps import QuestionAnswerConfig

app_name = QuestionAnswerConfig.name

urlpatterns = [
    path("ajax/createQuestion/", create_question, name="create_question"),
    path("ajax/activeQuestion/", active_question, name="active_question"),
    path("ajax/answerQuestion/", answer_question, name="answer_question"),
    path("ajax/createTimetable", create_timetable, name="create_timetable"),
]
