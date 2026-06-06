from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from django.shortcuts import get_object_or_404

from apps.courses.models import Course, Lesson
from .serializers import (
    CourseSerializer,
    LessonListSerializer,
    LessonDetailSerializer,
)


class CourseListAPIView(ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    search_fields = ["title"]
    ordering_fields = ["title"]


class CourseLessonsAPIView(ListAPIView):
    serializer_class = LessonListSerializer

    def get_queryset(self):
        return (
            Lesson.objects
            .filter(course_id=self.kwargs["course_id"])
            .order_by("order")
        )


class LessonDetailAPIView(ListAPIView):

    def get(self, request, lesson_id):
        lesson = get_object_or_404(
            Lesson.objects.prefetch_related("sections__blocks"), id=lesson_id
        )

        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)
