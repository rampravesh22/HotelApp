from django.contrib import admin
from home.models import Hotel, HotelBooking, HotelImages, Amenities
# Register your models here.


@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    list_display = ['hotel_name','hotel_price', 'description', 'room_count', ]


@admin.register(HotelBooking)
class HotelBookingAdmin(admin.ModelAdmin):
    list_display = ('hotel', 'user', 'start_date', 'end_date', 'booking_type')


@admin.register(HotelImages)
class HotelImagesAdmin(admin.ModelAdmin):
    list_display = ['images']

@admin.register(Amenities)
class AmenitiesAdmin(admin.ModelAdmin):
    list_display = ['amenity_name']

