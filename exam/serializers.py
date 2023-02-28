from rest_framework import serializers

from base.base_serializers import ModelSerializer

from .models import *


class ChoiceOfMultipleChoiceQuestionSerializer(ModelSerializer):
    class Meta:
        model = ChoiceOfMultipleChoiceQuestion
        fields = '__all__'


class QuestionSerializer(ModelSerializer):
    multiple_choice_questions = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_multiple_choice_questions(self, obj):
        return ChoiceOfMultipleChoiceQuestionSerializer(
            obj.choiceofmultiplechoicequestion_set.filter(is_active=True),
            many=True).data


class MultipleChoiceAnswerSerializer(ModelSerializer):
    class Meta:
        model = MultipleChoiceAnswer
        fields = '__all__'


class DescriptiveAnswerSerializer(ModelSerializer):
    class Meta:
        model = DescriptiveAnswer
        fields = '__all__'


class FileAnswerSerializer(ModelSerializer):
    class Meta:
        model = FileAnswer
        fields = '__all__'


class ExamSerializer(ModelSerializer):
    related_questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'


class UserExamSerializer(ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Exam
        fields = '__all__'
