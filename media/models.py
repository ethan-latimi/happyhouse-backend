from django.db import models
from common.models import CommonModel


class Photo(CommonModel):

    file = models.FileField()
    introduction = models.ForeignKey(
        "introductions.Introduction",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )
    notice = models.ForeignKey(
        "notices.Notice",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="photos",
    )

    def __str__(self):
        return "Photo File"
