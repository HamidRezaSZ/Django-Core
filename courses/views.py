from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from base.viewsets import ModelViewSet

from .filters import CourseFilter
from .models import *
from .serializers import *


class CourseCategoryView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = CourseCategory.objects.filter(is_active=True)
    serializer_class = CourseCategorySerializer

    filterset_fields = ['show_on_home_page']
    search_fields = ['title', 'description']


class CourseView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    queryset = Course.objects.filter(is_active=True)

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CourseItemSerializer

        return CourseSerializer

    filterset_class = CourseFilter
    search_fields = ['title', 'description', 'page']


class LessonView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Lesson.objects.filter(is_active=True)
    serializer_class = LessonSerializer

    search_fields = ['title', 'description']


class ChapterView(ModelViewSet):
    permission_classes_by_action = {
        "list": [AllowAny],
        "retrieve": [AllowAny],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }
    queryset = Chapter.objects.filter(is_active=True)
    serializer_class = ChapterSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    search_fields = ['title']


class NoteView(ModelViewSet):
    permission_classes_by_action = {
        "list": [IsAuthenticated],
        "retrieve": [IsAuthenticated],
        "create": [IsAdminUser],
        "update": [IsAdminUser],
        "partial_update": [IsAdminUser],
        "destroy": [IsAdminUser],
    }

    def get_queryset(self):
        return Note.objects.filter(is_active=True, participants=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(Note, pk=pk, participants=self.request.user, is_active=True)

    serializer_class = NoteSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context

    search_fields = ['description']


class NoteTakingView(ModelViewSet):
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return NoteTaking.objects.filter(user=self.request.user)

    def get_object(self):
        pk = self.kwargs['pk']
        return get_object_or_404(NoteTaking, user=self.request.user, pk=pk)

    serializer_class = NoteTakingSerializer

    filterset_fields = ['note']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"user": self.request.user})
        return context
