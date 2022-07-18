from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Hotel, HotelBooking, HotelImages, Amenities
from django.contrib.auth.decorators import login_required


# Create your views here.

@login_required(redirect_field_name="home/home.html")
def home(request):
    # print(Hotel._meta.fields)
    return render(request, "home/home.html")


def login_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user_obj = User.objects.filter(username=email)
        if not user_obj.exists():
            messages.warning(request, 'Account not found.')
            return redirect('home/register.html')
        user_log = authenticate(request,username=email, password=password)
        if not user_log:
            messages.warning(request, 'Inavlid username or password.')
            return redirect('home/login.html')
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
            return redirect('home/register.html')
        user = User()
        user.username = email
        user.set_password(user)
        user.save()
        return redirect("home/login.html")
    return render(request, "home/register.html", {})
