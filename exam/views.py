from base.viewsets import ModelViewSet
from .serializers import *
from .models import *
from rest_framework.permissions import IsAdminUser, IsAuthenticated


class MultipleChoiceAnswerView(ModelViewSet):
    serializer_class = MultipleChoiceAnswerSerializer
    queryset = MultipleChoiceAnswer.objects.all()
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "post": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }


class DescriptiveAnswerView(ModelViewSet):
    serializer_class = DescriptiveAnswerSerializer
    queryset = DescriptiveAnswer.objects.all()
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "post": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }


class FileAnswerView(ModelViewSet):
    serializer_class = FileAnswerSerializer
    queryset = FileAnswer.objects.all()
    permission_classes_by_action = {
        "list": [IsAdminUser],
        "retrieve": [IsAdminUser],
        "post": [IsAuthenticated],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }


class ExamView(ModelViewSet):
    serializer_class = ExamSerializer
    queryset = Exam.objects.filter(is_active=True)
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "post": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
