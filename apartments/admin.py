from django.contrib import admin
from . models import Apartment

# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["Name", "Ciudad"]
    list_filter = ["Ciudad"]

admin.site.register(Apartment, ApartmentAdmin)