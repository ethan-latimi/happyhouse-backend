from django.db import models
from common.models import CommonModel

# 각 사업 기능에 대한 예약 Model


class Reservation(CommonModel):

    """Reservation Model Definition"""

    class BusinessChoices(models.TextChoices):
        preschool = ("preschool", "Happy Preschool")
        housing = ("housing", "Happy Housing")
        farm = ("farm", "Happy farm")
        salon = ("salon", "Happy Hair Salon")

    business = models.CharField(
        max_length=255, choices=BusinessChoices.choices)
    user = models.ForeignKey("users.user", on_delete=models.CASCADE)
    check_in = models.DateField(
        null=True,
        blank=True,
    )
    check_out = models.DateField(
        null=True,
        blank=True,
    )
    guests = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.business.capitalize()} / booking for: {self.user}"
