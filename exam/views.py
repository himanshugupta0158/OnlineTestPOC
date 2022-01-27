from xml.dom import NotFoundErr
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from TestApp.permissions import IsAuthenticatedExaminer, IsAuthenticatedExaminee
from rest_framework.generics import ListAPIView, DestroyAPIView, CreateAPIView, RetrieveAPIView, \
    UpdateAPIView
from accounts.models import User

from exam.models import Exam_Detail, MCQ, Solution, Exam_Schedule
from exam.serializers import SolutionSerializer, MCQSerializer, ExamDetailSerializer, ExamScheduleSerializer


# Creating Exam
class ExamDetailCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = ExamDetailSerializer
    queryset = Exam_Detail.objects.all()

    def create(self, request, *args, **kwargs):
        data = request.data.copy()
        data['examiner'] = request.user.id
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

# Showing Exam list


class ExamDetailListView(ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ExamDetailSerializer

    def get_queryset(self):
        me = self.request.GET.get('me')
        uid = self.request.GET.get('id')
        if me:
            Exam_Detail.objects.filter(examiner=self.request.user)
        elif uid:
            Exam_Detail.objects.filter(examiner__id=uid)
        else:
            return Exam_Detail.objects.all()

# Creating Question and Options
class MCQCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = MCQSerializer
    queryset = MCQ.objects.all()


# Creating Solution for Existing Question in MCQ
class SolutionCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminer,)
    serializer_class = SolutionSerializer
    queryset = Solution.objects.all()
    

# Creating Test for time and Date for exam
class ExamScheduleCreateView(CreateAPIView):
    permission_classes = (IsAuthenticatedExaminee,)
    serializer_class = ExamScheduleSerializer
    queryset = Exam_Schedule.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
