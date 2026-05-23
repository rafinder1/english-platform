from django.db import models


class Section(models.Model):

    class Type(models.TextChoices):
        WARMUP = "warmup"
        MAIN = "main"
        REVISION = "revision"

    lesson = models.ForeignKey(
        "courses.Lesson", on_delete=models.CASCADE, related_name="sections"
    )

    type = models.CharField(max_length=20, choices=Type.choices)
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ["order"]
