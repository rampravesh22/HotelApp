from django.contrib import admin
from home.models import Hotel, HotelBooking, HotelImages, Amenities
# Register your models here.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Hotel._meta.fields if field.name != 'uid']


@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HotelBooking._meta.fields if field.name != 'uid']


@admin.register(HotelImages)
class HotelImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in HotelImages._meta.fields if field.name != 'uid']


@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Amenities._meta.fields if field.name != 'uid']
