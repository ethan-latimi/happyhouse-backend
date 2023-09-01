from django.db import models
from common.models import CommonModel

# 각각의 사업(preschool, housing, farm, hairsalon)들 소개란


class introduction(CommonModel):

    """ Business Introduction model Defined """

    class BusinessChoices(models.TextChoices):
        preschool = ("preschool", "Happy Preschool")
        housing = ("housing", "Happy Housing")
        farm = ("farm", "Happy farm")
        salon = ("salon", "Happy Hair Salon")

    kind = models.CharField(
        max_length=20,
        choices=BusinessChoices.choices,
    )
    description = models.TextField()

    def __str__(self):
        return f"{self.kind.capitalize()} Introduction"
