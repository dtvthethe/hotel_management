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
    path('guestbookingdetail/<int:pk>', views.GuestBookingRetrieveAPIView().as_view(), name='guestbookingdetail'),
    path('reveration_update/<int:pk>', views.ReverationUpdateAPIView().as_view(), name='reverationupdate'),
    path('booking_update/<int:pk>', views.BookingUpdateAPIView().as_view(), name='bookingupdate'),
    path('reveration_delete/<int:pk>', views.BookingDestroyAPIView.as_view(), name='reverationdelete'),
]

