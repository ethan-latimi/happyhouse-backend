from django.contrib import admin
from .models import Notice, Comment


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
