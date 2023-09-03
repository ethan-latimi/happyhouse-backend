from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'file', 'introduction',
                    'notice', 'created_at', 'updated_at')
    list_filter = ('introduction', 'notice', 'created_at', 'updated_at')
    search_fields = ('id', 'file')
    date_hierarchy = 'created_at'
