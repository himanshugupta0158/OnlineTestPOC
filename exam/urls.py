from django.urls import path

from exam.views import ExamDetailCreateView, MCQCreateView, ExamDetailListView, SolutionCreateView, ExamScheduleCreateView

app_name = 'exam'

urlpatterns = [
    path('create/', ExamDetailCreateView.as_view()),
    path('list/', ExamDetailListView.as_view()),
    path('create-mcq/', MCQCreateView.as_view()),
    path('add-solution/', SolutionCreateView.as_view()),
    path("add-schedule/", ExamScheduleCreateView.as_view()),
]
