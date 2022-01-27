from django.db import models


# Create your models here.
from accounts.models import User


class Exam_Detail(models.Model):
    examiner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=64)
    info = models.TextField()
    duration = models.DurationField(help_text="hr:min:sec = 00:00:00")

    def __str__(self):
        return self.name


class MCQ(models.Model):
    question = models.TextField()
    option1 = models.CharField(max_length=15)
    option2 = models.CharField(max_length=15)
    option3 = models.CharField(max_length=15)
    option4 = models.CharField(max_length=15)

    def __str__(self):
        return self.question


class Solution(models.Model):
    exam = models.ForeignKey(
        Exam_Detail, on_delete=models.CASCADE, related_name='questions')
    question = models.ForeignKey(
        MCQ, on_delete=models.CASCADE, related_name='questions')
    answer = models.CharField(max_length=15)

    def __str__(self):
        return self.answer


class Exam_Schedule(models.Model):
    exam = models.ForeignKey(Exam_Detail, on_delete=models.CASCADE)
    start_time = models.DateTimeField(null=True)
