from django.db import models
from common.models import CommonModel
from django.core.exceptions import ValidationError


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

    def clean(self):
        if self.introduction and self.notice:
            raise ValidationError(
                "You can choose either an introduction or a notice, not both.")
