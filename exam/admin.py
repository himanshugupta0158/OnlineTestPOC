from django.contrib import admin
from exam.models import Exam, Question, Option, Answer
# Register your models here.

admin.site.register(Exam)
admin.site.register(Question)
admin.site.register(Option)
admin.site.register(Answer)
