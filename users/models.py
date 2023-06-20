from django.db import models
from django.contrib.auth.models import AbstractUser

# 웹사이트 회원 Model

class User(AbstractUser):
    
    """User Model Definition"""

    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    first_name = models.CharField(
        max_length=150,
    )
    last_name = models.CharField(
        max_length=150,
    )
    avatar = models.URLField(null=True, blank=True)
    is_resident = models.BooleanField(default=False)
    is_parent= models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
        default="male",
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
        default="en",
    )
    email = models.EmailField()

