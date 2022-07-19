from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from home.models import Hotel, HotelBooking, HotelImages, Amenities
from django.contrib.auth.decorators import login_required


# Create your views here.
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
            return redirect('/login/')
        user_log = authenticate(request,username=email, password=password)
        if not user_log:
            messages.warning(request, 'Inavlid username or password.')
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
        messages.success(request, "Congratulations!! You have registered successfully.")
        return redirect("/login/")
    return render(request, "home/register.html", {})

