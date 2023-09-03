from django.contrib import admin
from .models import Introduction


@admin.register(Introduction)
class IntroductionAdmin(admin.ModelAdmin):
    pass
