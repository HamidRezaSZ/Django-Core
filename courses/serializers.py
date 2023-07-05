from rest_framework import serializers

from base.base_serializers import ModelSerializer

from .models import *


class CourseCategorySerializer(ModelSerializer):
    class Meta:
        model = CourseCategory
        fields = '__all__'


class TeacherSerializer(ModelSerializer):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseSerializer(ModelSerializer):
    teacher = TeacherSerializer()

    class Meta:
        model = Course
        fields = ('id', 'title', 'image', 'price', 'slug', 'teacher')


class CourseItemSerializer(ModelSerializer):
    teacher = TeacherSerializer()
    category = CourseCategorySerializer()
    lessons = serializers.SerializerMethodField()
    is_buy = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, obj):
        user = self.context.get('user')
        return LessonSerializer(
            obj.lesson_set.filter(is_active=True),
            many=True, context={'user': user}).data

    def get_is_buy(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return obj.full_access_user(user)
        return False


class LessonSerializer(ModelSerializer):
    chapters = serializers.SerializerMethodField()
    is_buy = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = '__all__'

    def get_chapters(self, obj):
        user = self.context.get('user')
        return ChapterSerializer(
            obj.chapter_set.filter(is_active=True),
            many=True, context={'user': user}).data

    def get_is_buy(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return obj.full_access_user(user)
        return False


class ChapterSerializer(ModelSerializer):
    notes = serializers.SerializerMethodField()
    is_buy = serializers.SerializerMethodField()

    class Meta:
        model = Chapter
        fields = '__all__'

    def get_notes(self, obj):
        user = self.context.get('user')
        return NoteSerializer(
            obj.note_set.filter(is_active=True), context={'user': user},
            many=True).data

    def get_is_buy(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return obj.full_access_user(user)
        return False


class NoteSerializer(ModelSerializer):
    is_buy = serializers.SerializerMethodField()

    class Meta:
        model = Note
        exclude = ('participants',)

    def get_is_buy(self, obj):
        user = self.context.get('user')
        if user.is_authenticated:
            return obj.full_access_user(user)
        return False


class NoteTakingSerializer(ModelSerializer):
    class Meta:
        model = NoteTaking
        exclude = ('user',)

    def create(self, validated_data):
        user = self.context.get('user')
        validated_data['user'] = user
        note_taking_obj = NoteTaking.objects.filter(
            user=user, note=validated_data['note'])
        if note_taking_obj.exists():
            note_taking_obj = note_taking_obj.first()
            note_taking_obj.content = validated_data['content']
            note_taking_obj.save()
            return note_taking_obj

        return super().create(validated_data)
