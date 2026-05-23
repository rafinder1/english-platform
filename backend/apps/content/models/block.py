from django.db import models


class ContentBlock(models.Model):

    class BlockType(models.TextChoices):
        HEADING = "heading", "Heading"
        TEXT = "text", "Text"
        IMAGE = "image", "Image"
        LIST = "list", "List"

    section = models.ForeignKey(
        "content.Section", on_delete=models.CASCADE, related_name="blocks"
    )

    type = models.CharField(max_length=30, choices=BlockType.choices)

    order = models.PositiveIntegerField()

    data = models.JSONField(default=dict)

    class Meta:
        ordering = ["order"]

    def __str__(self):
        return f"{self.type} block"
