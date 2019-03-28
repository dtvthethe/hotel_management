from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('rooms', views.RoomListAPIView().as_view(), name='roomlist'),
    path('guest_bookings', views.GuestBookingListAPIView().as_view(), name='guestlist'),
    path('room_roomtypes', views.RoomRoomTypesListAPIView().as_view(), name='roomroomtypeslist'),
    path('guest_booking', views.GuestBookingFOListAPIView().as_view(), name='guestbooking'),
    path('guest_create', views.GuestCreateAPIView().as_view(), name='guestcreate'),
    path('new_reveration', views.BokingCreateAPIView().as_view(), name='createreveration'),
    path('clients', views.ClientListAPIView().as_view(), name='clientlist'),
    path('roomtypes', views.RoomRoomTypesListAPIView().as_view(), name='roomtypelist'),
]