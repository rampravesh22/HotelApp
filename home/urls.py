from django.urls import path, include
from home import views
urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login_page, name="login"),
    path('register/', views.register_page, name="register"),
    path('hoteldetail/<slug:uid>/', views.hotel_detail, name="hoteldetail"),
    path('check-booking/', views.check_booking, name="check-booking"),

]
