from django.contrib import admin
from .models import notice


@admin.register(notice)
class NoticeAdmin(admin.ModelAdmin):
    pass
