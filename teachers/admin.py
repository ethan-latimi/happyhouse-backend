from django.contrib import admin
from .models import teacher


@admin.register(teacher)
class TeacherAdmin(admin.ModelAdmin):
    pass
