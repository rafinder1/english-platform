from django.db import models


class Lesson(models.Model):
    course = models.ForeignKey("courses.Course", on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    order = models.IntegerField()

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return self.title
