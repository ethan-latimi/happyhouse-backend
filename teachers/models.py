from django.db import models
from common.models import CommonModel

# 선생님 정보 Model


class Teacher(CommonModel):

    """Teacher Model Definition"""

    nick_name = models.CharField(max_length=50)
    bio = models.TextField()
    photo = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.nick_name
