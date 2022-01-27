from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule


class MCQSerializer(ModelSerializer):

    def validate_question(self, value):
        if value not in MCQ.objects.filter(exam__examiner=self.context.get('request').user):
            raise serializers.ValidationError(
                "Can Only Add options to own exam's questions")
        return value

    class Meta:
        model = MCQ
        fields = '__all__'


class SolutionSerializer(ModelSerializer):

    def validate_exam(self, value):
        if value not in self.context.get('request').user.exams.all():
            raise serializers.ValidationError(
                "Please create exam because you Can Only Add questions to own exams")
        return value

    class Meta:
        model = Solution
        fields = '__all__'


class ExamDetailSerializer(ModelSerializer):
    class Meta:
        model = Exam_Detail
        fields = '__all__'


class ExamScheduleSerializer(ModelSerializer):
    class Meta:
        model = Exam_Schedule
        fields = '__all__'
