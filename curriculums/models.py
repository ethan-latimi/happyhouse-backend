from django.db import models
from common.models import CommonModel
# 어린이집이 가지고 있는 학습 커리큘럼 model

class curriculum(CommonModel):

    """Curriculum Model Definition"""

    title = models.CharField(max_length=255)
    description = models.TextField()
    photo=models.URLField()

    def __str__(self):
        return self.title