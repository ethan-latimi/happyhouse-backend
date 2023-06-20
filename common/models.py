from django.db import models

# 재사용성을 위한 common model *model 상속과 class Meta -> abstract = True가 핵심 요소

class CommonModel(models.Model):

    """Common Model Definition"""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
