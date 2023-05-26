from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated

from base.viewsets import ModelViewSet

from .models import *
from .serializers import *


class ExamView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self):
        query = [exam for exam in Exam.objects.filter(is_active=True) if exam.content_type.get_object_for_this_type(
            id=exam.object_id).full_access_user(self.request.user)]
        [UserExam.objects.get_or_create(
            exam=exam, user=self.request.user) for exam in query]

        return Exam.objects.filter(id__in=[exam.id for exam in query])

    filterset_fields = {'parent': ['exact', 'isnull'],
                        'object_id': ['exact'], 'content_type': ['exact']}

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return ExamItemSerializer
        return ExamSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context


class UserAnswerView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "create": [IsAuthenticated],
        "update": [IsAuthenticated],
        "partial_update": [IsAuthenticated],
        "destroy": [IsAuthenticated],
    }

    def get_queryset(self):
        return UserAnswer.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    filterset_fields = ['exam', 'question']
    serializer_class = UserAnswerSerializer


class ResultView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self):
        return Result.objects.filter(user=self.request.user)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    filterset_fields = {'parent': ['exact', 'isnull'],
                        'exam': ['exact']}
    serializer_class = ResultSerializer


class DescriptiveAnswerView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self):
        user_exam_id = UserExam.objects.filter(
            user=self.request.user).values_list('exam', flat=True)
        return DescriptiveAnswer.objects.filter(is_active=True, exam__in=user_exam_id)

    filterset_fields = ['exam']
    serializer_class = DescriptiveAnswerSerializer
