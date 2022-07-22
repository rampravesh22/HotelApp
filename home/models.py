from audioop import reverse
from django.db import models
import uuid
from django.contrib.auth.models import User
# Create your models here.


class BaseModel(models.Model):
    uid = models.UUIDField(
        default=uuid.uuid4, editable=False, primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)

    class Meta:
        abstract = True


class Amenities(BaseModel):
    amenity_name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.amenity_name


class Hotel(BaseModel):
    amenities = models.ManyToManyField(
        Amenities, related_name="hotel_amenities")
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.FloatField()
    description = models.TextField()
    room_count = models.IntegerField(default=10)

    def __str__(self) -> str:
        return self.hotel_name


class HotelImages(BaseModel):
    hotel = models.ForeignKey(
        Hotel, related_name="hotel_images", on_delete=models.CASCADE)
    images = models.ImageField(upload_to="hotel")
    name = models.CharField(max_length=100, default="")


class HotelBooking(BaseModel):
    booking_type_choice = (
        ("Pre Paid", 'Prepaid'),
        ("Post Paid", 'Postpaid')
    )
    hotel = models.ForeignKey(
        Hotel, related_name="hotel_booking", on_delete=models.CASCADE)
    user = models.ForeignKey(
        User, related_name="user", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(
        max_length=100, choices=booking_type_choice)
