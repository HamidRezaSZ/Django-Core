import django_filters
from django_filters import FilterSet

from .models import Course, Note


class CourseFilter(FilterSet):
    is_my_course = django_filters.BooleanFilter(
        label='is_my_course',  method='filter_is_my_course')

    class Meta:
        model = Course
        fields = {
            'category': ['exact'],
        }

    def filter_is_my_course(self, queryset, name, value):
        courses = []
        for item in Note.objects.filter(participants=self.request.user):
            courses.append(item.chapter.lesson.course.id)

        return queryset.filter(id__in=courses)
