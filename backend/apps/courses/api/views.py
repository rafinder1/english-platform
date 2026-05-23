from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from apps.courses.models import Course, Lesson
from .serializers import (
    CourseSerializer,
    LessonListSerializer,
    LessonDetailSerializer,
)


class CourseListAPIView(APIView):

    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)


class CourseLessonsAPIView(APIView):

    def get(self, request, course_id):
        lessons = Lesson.objects.filter(course_id=course_id).order_by("order")
        serializer = LessonListSerializer(lessons, many=True)
        return Response(serializer.data)


class LessonDetailAPIView(APIView):

    def get(self, request, lesson_id):
        lesson = get_object_or_404(
            Lesson.objects.prefetch_related("sections__blocks"), id=lesson_id
        )

        serializer = LessonDetailSerializer(lesson)
        return Response(serializer.data)
