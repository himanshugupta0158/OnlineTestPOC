from django.contrib import admin
from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule
# Register your models here.

admin.site.register(Exam_Detail)
admin.site.register(Exam_Schedule)
admin.site.register(Solution)
admin.site.register(MCQ)
