from django.contrib import admin
from .models import reservation


@admin.register(reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass
