from django.contrib import admin
from .models import introduction


@admin.register(introduction)
class IntroductionAdmin(admin.ModelAdmin):
    pass
