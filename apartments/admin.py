from django.contrib import admin
from . models import Apartment, ApartmentCountry, ApartmentCity, ApartmentNeighborhood, ApartmentPicture , Room, ApartmentAmenity, ApartmentNew

# Register your models here.

class ApartmentAdmin(admin.ModelAdmin):
    list_display = ["Name", "Ciudad"]
    list_filter = ["Ciudad"]

admin.site.register(Apartment, ApartmentAdmin)

@admin.register(ApartmentCountry)
class ApartmentCountryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(ApartmentCity)
class ApartmentCityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'country')
    list_filter = ('country',)
    search_fields = ('name',)
    def has_change_permission(self, request, obj = ...):
        return False

@admin.register(ApartmentNeighborhood)
class ApartmentNeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city')
    list_filter = ('city',)
    search_fields = ('name',)

class ApartmentPictureInline(admin.TabularInline):
    model = ApartmentPicture
    extra = 1

class RoomInline(admin.TabularInline):
    model = Room
    extra = 1

class ApartmentAmenityInline(admin.TabularInline):
    model = ApartmentAmenity
    extra = 1

@admin.register(ApartmentNew)
class ApartmentNewAdmin(admin.ModelAdmin):
    list_display = ('title', 'city', 'country', 'neighborhood', 'active')
    list_filter = ('city', 'active')
    search_fields = ('title', 'city', 'neighborhood')
    inlines = [ApartmentPictureInline, RoomInline, ApartmentAmenityInline]

# @admin.register(Room)
# class RoomAdmin(admin.ModelAdmin):
#     list_display = ('apartment', 'room_number')

# @admin.register(Bed)
# class BedAdmin(admin.ModelAdmin):
#     list_display = ('room', 'type', 'quantity')

# @admin.register(Amenity)
# class AmenityAdmin(admin.ModelAdmin):
#     list_display = ('name',)

# @admin.register(ApartmentAmenity)
# class ApartmentAmenityAdmin(admin.ModelAdmin):
#     list_display = ('apartment', 'amenity')