from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Hotel, HotelBooking, HotelImages, Amenities
from django.contrib.auth.decorators import login_required
from .models import Hotel, HotelBooking, Amenities, HotelImages
from django.db.models import Q
# Create your views here.


def home(request):
    amenities_obj = Amenities.objects.all()
    hotel_obj = Hotel.objects.all()
    sort_by = request.GET.get('sort-by')
    search = request.GET.get('search')
    print(search)
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
        for hotel in hotel_obj:
            print(hotel.hotel_name)

    context = {
        'amenities_obj': amenities_obj,
        "hotel_obj": hotel_obj,
        'sort_by': sort_by

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


print("*****************************************************")

print("*****************************************************")
