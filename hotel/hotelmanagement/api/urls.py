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

    path('product_types', views.ProductTypesListAPIView().as_view(), name='producttypes'),
    path('products', views.ProductListAPIView().as_view(), name='products'),

    path('minibarcharge', views.MinibarChargeListAPIView().as_view(), name='minibarcharge'),
    path('minibarcharge_create', views.MinibarChargeCreateAPIView().as_view(), name='minibarchargecreate'),
    path('minibarcharge_update/<int:pk>', views.MinibarChargeUpdateAPIView().as_view(), name='minibarchargeupdate'),
    path('minibarcharge_delete/<int:pk>', views.MinibarChargeDestroyAPIView().as_view(), name='minibarchargecdelete'),

    path('bookingpayment', views.BookingPaymentListAPIView().as_view(), name='bookingpayment'),
    path('bookingpayment_create', views.BookingPaymentCreateAPIView().as_view(), name='bookingpaymentcreate'),
    path('bookingpayment_update/<int:pk>', views.BookingPaymentUpdateAPIView().as_view(), name='bookingpaymentupdate'),
    path('bookingpayment_delete/<int:pk>', views.BookingPaymentDestroyAPIView().as_view(), name='bookingpaymentdelete'),

    path('roomcharge', views.RoomChargeListAPIView().as_view(), name='roomcharge'),
    path('roomcharge_create', views.RoomChargeCreateAPIView().as_view(), name='roomchargecreate'),
    path('roomcharge_update/<int:pk>', views.RoomChargeUpdateAPIView().as_view(), name='roomchargeupdate'),
    path('roomcharge_delete/<int:pk>', views.RoomChargeDestroyAPIView().as_view(), name='roomchargedelete'),

]

