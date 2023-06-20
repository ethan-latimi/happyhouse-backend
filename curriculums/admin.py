from django.contrib import admin
from .models import curriculum


@admin.register(curriculum)
class CurriculumAdmin(admin.ModelAdmin):
    pass
