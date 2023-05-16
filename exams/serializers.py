from django.db.models import Max, Min
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from rest_framework import serializers

from base.base_serializers import ModelSerializer

from .models import *


class SubExamSerializer(ModelSerializer):
    no_all_questions = serializers.SerializerMethodField()
    no_done_questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = ('id', 'title', 'no_all_questions', 'no_done_questions')

    def get_no_all_questions(self, obj):
        return obj.question_set.count()

    def get_no_done_questions(self, obj):
        user = self.context['user']
        return UserQuestion.objects.filter(exam=obj, user=user).count()


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        exclude = ('correct_answer',)


class DescriptiveAnswerSerializer(ModelSerializer):
    class Meta:
        model = DescriptiveAnswer
        fields = '__all__'


class ExamItemSerializer(ModelSerializer):
    questions = serializers.SerializerMethodField()
    no_all_questions = serializers.SerializerMethodField()
    no_done_questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        exclude = ('parent',)

    def get_questions(self, obj):
        return QuestionSerializer(obj.question_set.filter(is_active=True), many=True).data

    def get_no_all_questions(self, obj):
        return obj.question_set.count()

    def get_no_done_questions(self, obj):
        user = self.context['user']
        return UserQuestion.objects.filter(exam=obj, user=user).count()


class ExamSerializer(ModelSerializer):
    sub_exams = serializers.SerializerMethodField()
    questions = serializers.SerializerMethodField()

    class Meta:
        model = Exam
        fields = '__all__'

    def get_sub_exams(self, obj):
        user = self.context['user']
        return SubExamSerializer(obj.child.filter(is_active=True), many=True, context={'user': user}).data

    def get_questions(self, obj):
        return QuestionSerializer(obj.question_set.filter(is_active=True), many=True).data


class UserQuestionSerializer(ModelSerializer):
    class Meta:
        model = UserQuestion
        exclude = ('user',)

    def validate(self, attrs):
        user = self.context['user']
        exam = attrs['exam']
        if not exam.content_type.get_object_for_this_type(id=exam.object_id).full_access_user(user):
            raise serializers.ValidationError(
                _('You dont permission to start this exam'))

        duration = exam.duration
        user_exam_obj = get_object_or_404(
            UserExam, user=user, exam=exam)

        if exam.parent:
            user_exam_obj = get_object_or_404(
                UserExam, user=user, exam=exam.parent)
            duration = exam.parent.duration

        if timezone.now() > user_exam_obj.created_date + duration:
            raise serializers.ValidationError(_('Exam has finished'))

        return super().validate(attrs)

    def create(self, validated_data):
        user = self.context['user']
        validated_data['user'] = user
        item = UserQuestion.objects.filter(
            user=user, exam=validated_data['exam'], question=validated_data['question'])
        if item.exists():
            item = item.first()
            item.answer = validated_data['answer']
            item.save()
            return item

        return super().create(validated_data)


class SubResultSerializer(ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Result
        exclude = ('user',)


class ResultSerializer(ModelSerializer):
    sub_result = serializers.SerializerMethodField()
    max_result = serializers.SerializerMethodField()
    min_result = serializers.SerializerMethodField()
    exam = ExamSerializer()

    class Meta:
        model = Result
        exclude = ('user',)

    def get_sub_result(self, obj):
        user = self.context['user']
        return SubResultSerializer(obj.child.filter(is_active=True), many=True, context={'user': user}).data

    def get_max_result(self, obj):
        return Result.objects.filter(exam=obj.exam).aggregate(Max('score'))['score__max']

    def get_min_result(self, obj):
        return Result.objects.filter(exam=obj.exam).aggregate(Min('score'))['score__min']
