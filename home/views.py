from django.shortcuts import render
from home.models import Hotel, HotelBooking, HotelImages, Amenities
# Create your views here.
def home(request):
    # print(Hotel._meta.fields)
    return render(request,"hotel.html")