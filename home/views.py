from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Hotel, HotelBooking, HotelImages, Amenities
from django.contrib.auth.decorators import login_required
from .models import Hotel, HotelBooking, Amenities, HotelImages
from django.db.models import Q
# Create your views here.
print("**********************************************************")


def home(request):
    amenities_obj = Amenities.objects.all()
    hotel_obj = Hotel.objects.all()
    sort_by = request.GET.get('sort-by')
    search = request.GET.get('search')
    if sort_by:
        if sort_by == "asc":
            hotel_obj = hotel_obj.order_by('hotel_price')
            asc = "selected"
            desc = ""
        elif sort_by == "desc":
            hotel_obj = hotel_obj.order_by('-hotel_price')
            desc = 'selected'
            asc = ""
    if search:
        hotel_obj = hotel_obj.filter(
            Q(hotel_name__icontains=search) | Q(description=search))

    amenities = request.GET.getlist('amenity')
    if len(amenities):
        hotel_obj = hotel_obj.filter(
            amenities__amenity_name__in=amenities).distinct()
    context = {
        'amenities_obj': amenities_obj,
        "hotel_obj": hotel_obj,
        'sort_by': sort_by,
        'search': search,
        'amenities': amenities

    }
    return render(request, "home/home.html", context)


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return redirect('/login/')
        user_log = authenticate(request, username=email, password=password)
        if not user_log:
            messages.warning(request, 'In-valid username or password.')
            return redirect('/login/')
        login(request, user_log)
        return redirect('/')
    return render(request, 'home/login.html')


def register_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if user_obj.exists():
            messages.warning(request, 'User name already exists.')
            return redirect('/register/')
        user = User()
        user.username = email
        user.set_password(password)
        user.save()
        messages.success(
            request, "Congratulations!! You have registered successfully.")
        return redirect("/login/")
    return render(request, "home/register.html", {})


def check_booking(start_date, end_date, uid, room_count):
    qs = HotelBooking.objects.filter(
        start_date__lte=start_date, end_date__gte=end_date, hotel__uid=uid)
    print(qs.values())
    print(len(qs))
    if len(qs) >= room_count:
        return False
    return True


def hotel_detail(request, uid):
    hotel_object = Hotel.objects.get(uid=uid)
    if request.method == "POST":
        checkin = request.POST.get('checkin')
        checkout = request.POST.get('checkout')
        if checkin > checkout:
            messages.warning(request, "Enter proper date to book !")
            return redirect(request.META.get('HTTP_REFERER'))
        s = HotelBooking(hotel=hotel, user=request.user,
                         start_date=checkin, end_date=checkout, booking_type="Prepaid")
        hotel = Hotel.objects.get(uid=uid)

        total_booked = 0
        if s.start_date > total_booked:
            messages.warning(request, "Please select proper date")
            return redirect(request.META.get('HTTP_REFERER'))

        if not check_booking(checkin, checkout, uid, hotel.room_count):
            messages.warning(
                request, "Sorry, No room is available in between thsese dates!")
            return redirect(request.META.get('HTTP_REFERER'))

        s.save()
        messages.success(request, "Your booking has been completed")
        return redirect(request.META.get('HTTP_REFERER'))

    context = {
        "hotels_obj": hotel_object
    }
    return render(request, "home/hotel_detail.html", context)


print("**********************************************************")
