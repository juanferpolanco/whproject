from django.contrib import admin
from reservations.models import Reservation

# Register your models here.

admin.site.register(Reservation)

# @admin.register(ReservationNew)
# class ReservationNewAdmin(admin.ModelAdmin):
#     list_display = ('apartment', 'user', 'start_date', 'end_date', 'total_price')