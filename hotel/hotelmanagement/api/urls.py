from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('rooms', views.RoomListAPIView().as_view(), name='roomlist'),
    path('guest_booking', views.GuestBookingListAPIView().as_view(), name='guestlist')
]