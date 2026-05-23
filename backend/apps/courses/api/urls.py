from django.urls import path
from .views import (
    CourseListAPIView,
    CourseLessonsAPIView,
    LessonDetailAPIView,
)

urlpatterns = [
    path("courses/", CourseListAPIView.as_view()),
    path("courses/<int:course_id>/lessons/", CourseLessonsAPIView.as_view()),
    path("lessons/<int:lesson_id>/", LessonDetailAPIView.as_view()),
]
