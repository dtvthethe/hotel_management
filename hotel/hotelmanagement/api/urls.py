from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('rooms', views.RoomListAPIView().as_view(), name='roomlist'),
    path('guest_bookings', views.GuestBookingListAPIView().as_view(), name='guestlist'),
    path('room_roomtypes', views.RoomRoomTypesListAPIView().as_view(), name='roomroomtypeslist'),
    path('guest_booking', views.GuestBookingFOListAPIView().as_view(), name='guestbooking'),
]