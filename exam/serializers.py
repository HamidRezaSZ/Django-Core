from rest_framework import serializers
from .models import *


class ChoiceOfMultipleChoiceQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChoiceOfMultipleChoiceQuestion
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    multiple_choice_questions = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = '__all__'

    def get_multiple_choice_questions(self, obj):
        return ChoiceOfMultipleChoiceQuestionSerializer(
            obj.choiceofmultiplechoicequestion_set.filter(is_active=True),
            many=True).data


class MultipleChoiceAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = MultipleChoiceAnswer
        fields = '__all__'


class DescriptiveAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescriptiveAnswer
        fields = '__all__'


class FileAnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileAnswer
        fields = '__all__'


class ExamSerializer(serializers.ModelSerializer):
    related_questions = QuestionSerializer(many=True)

    class Meta:
        model = Exam
        fields = '__all__'


class UserExamSerializer(serializers.ModelSerializer):
    exam = ExamSerializer()

    class Meta:
        model = Exam
        fields = '__all__'
