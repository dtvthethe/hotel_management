from django.urls import path
from django.conf.urls import url
from rest_framework_jwt.views import obtain_jwt_token, verify_jwt_token
from . import views

app_name = 'api'

urlpatterns = [
    path('config', views.ConfigListAPIView().as_view(), name='config'),

    path('rooms', views.RoomListAPIView().as_view(), name='roomlist'),

    path('guest_bookings', views.GuestBookingListAPIView().as_view(), name='guestlist'),
    path('guestbookingdetail/<int:pk>', views.GuestBookingRetrieveAPIView().as_view(), name='guestbookingdetail'),
    path('guest_booking', views.GuestBookingFOListAPIView().as_view(), name='guestbooking'),

    path('room_roomtypes', views.RoomRoomTypesListAPIView().as_view(), name='roomroomtypeslist'),
    path('guest_create', views.GuestCreateAPIView().as_view(), name='guestcreate'),
    path('new_reveration', views.BokingCreateAPIView().as_view(), name='createreveration'),
    path('clients', views.ClientListAPIView().as_view(), name='clientlist'),
    path('roomtypes', views.RoomRoomTypesListAPIView().as_view(), name='roomtypelist'),
    path('reveration_update/<int:pk>', views.ReverationUpdateAPIView().as_view(), name='reverationupdate'),
    path('booking_update/<int:pk>', views.BookingUpdateAPIView().as_view(), name='bookingupdate'),
    path('reveration_delete/<int:pk>', views.BookingDestroyAPIView.as_view(), name='reverationdelete'),

    path('product_types', views.ProductTypesListAPIView().as_view(), name='producttypes'),
    path('products', views.ProductListAPIView().as_view(), name='products'),

    # path('minibarcharge', views.MinibarChargeListAPIView().as_view(), name='minibarcharge'),
    # path('minibarchargebybooking', views.MinibarChargeByBookingListAPIView().as_view(), name='minibarchargebybooking'),
    # path('minibarcharge_create', views.MinibarChargeCreateAPIView().as_view(), name='minibarchargecreate'),
    # path('minibarcharge_detail/<int:pk>', views.MinibarChargeRetrieveAPIView().as_view(), name='minibarchargedetail'),
    # path('minibarcharge_update/<int:pk>', views.MinibarChargeUpdateAPIView().as_view(), name='minibarchargeupdate'),
    # path('minibarcharge_delete/<int:pk>', views.MinibarChargeDestroyAPIView().as_view(), name='minibarchargecdelete'),

    path('boookingbyfolio', views.BookingByFolioListAPIView.as_view(), name='boookingbyfolio'),
    path('checkin/<int:pk>', views.CheckInAPIView.as_view(), name='checkin'),
    path('booking_checkout/<int:pk>', views.BookingCheckOutUpdateAPIView.as_view(), name='bookingcheckout'),
    path('bookingbycondition', views.BookingDateNotAvailableListAPIView.as_view(), name='bookingbycondition'),

    path('bookingpayment', views.BookingPaymentListAPIView().as_view(), name='bookingpayment'),
    path('bookingpayment_create', views.BookingPaymentCreateAPIView().as_view(), name='bookingpaymentcreate'),
    path('bookingpayment_update/<int:pk>', views.BookingPaymentUpdateAPIView().as_view(), name='bookingpaymentupdate'),
    path('bookingpayment_delete/<int:pk>', views.BookingPaymentDestroyAPIView().as_view(), name='bookingpaymentdelete'),
    #
    # path('roomcharge', views.RoomChargeListAPIView().as_view(), name='roomcharge'),
    # path('roomcharge_create', views.RoomChargeCreateAPIView().as_view(), name='roomchargecreate'),
    # path('roomcharge_update_roomrate/<int:pk>', views.RoomChargeRateRoomUpdateAPIView().as_view(), name='roomchargeupdateroomrate'),
    # path('roomcharge_delete/<int:pk>', views.RoomChargeDestroyAPIView().as_view(), name='roomchargedelete'),

    path('paymenttypes', views.PaymentTypeListAPIView().as_view(), name='paymenttypes'),

    path('users', views.UserListAPIView().as_view(), name='users'),
    path('user_create', views.UserCreateAPIView().as_view(), name='user_create'),
    path('user/<int:pk>', views.UserRetrieveAPIView().as_view(), name='user_retrieve'),
    path('user_update/<int:pk>', views.UserUpdateAPIView().as_view(), name='user_update'),
    path('user_password/<int:pk>', views.UserPasswordUpdateAPIView().as_view(), name='user_password'),
    path('user_delete/<int:pk>', views.UserDestroyAPIView().as_view(), name='user_delete'),
    path('userpermissions', views.UserPermissionListAPIView().as_view(), name='userpermissions'),

    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),

    path('product2s', views.Product2ListAPIView().as_view(), name='product2s'),
    path('product/create', views.ProductCreateAPIView().as_view(), name='product2_create'),
    path('product/edit/<int:pk>', views.ProductUpdateAPIView().as_view(), name='product2_edit'),
    path('product/delete/<int:pk>', views.ProductDestroyAPIView().as_view(), name='product2_delete'),

    path('room2s', views.Room2ListAPIView().as_view(), name='room2s'),
    path('room/create', views.RoomCreateAPIView().as_view(), name='room2_create'),
    path('room/edit/<int:pk>', views.RoomUpdateAPIView().as_view(), name='room2_edit'),
    path('room/edit_roomstatus/<int:pk>', views.RoomStatusUpdateAPIView().as_view(), name='room2_edit'),
    path('room/delete/<int:pk>', views.RoomDestroyAPIView().as_view(), name='room2_delete'),


    path('room2types', views.Room2TypeListAPIView().as_view(), name='room2types'),
    path('room2type/create', views.RoomTypeCreateAPIView().as_view(), name='room2type_create'),
    path('room2type/edit/<int:pk>', views.RoomTypeUpdateAPIView().as_view(), name='room2type_edit'),
    path('room2type/delete/<int:pk>', views.RoomTypeDestroyAPIView().as_view(), name='room2type_delete'),

    path('product2types', views.ProductTypesListAPIView().as_view(), name='product2types'),
    path('product2type/create', views.ProductTypeCreateAPIView().as_view(), name='rproduct2type_create'),
    path('product2type/edit/<int:pk>', views.ProductTypeUpdateAPIView().as_view(), name='product2type_edit'),
    path('product2type/delete/<int:pk>', views.ProductTypeDestroyAPIView().as_view(), name='product2type_delete'),

    path('roomstatus', views.RoomStatusListAPIView().as_view(), name='room_status'),


    path('invoices', views.InvoiceListAPIView().as_view(), name='invoices'),
    path('invoice/updatefoliotransfer/<int:pk>', views.InvoiceFolioUpdateAPIView.as_view(), name='invoiceupdatefoliotransfer'),

    # path('invoicedetails', views.InvoiceDetailListAPIView().as_view(), name='invoicedetails'),
    path('invoicedetail/create', views.InvoiceDetailCreateAPIView().as_view(), name='invoicedetail_create'),
    path('invoicedetail/update/<int:pk>', views.InvoiceDetailUpdateAPIView().as_view(), name='invoicedetail_update'),
    path('invoicedetailprice/update/<int:pk>', views.InvoiceDetailPriceConfirmUpdateAPIView().as_view(), name='invoicedetailprice_update'),
    path('invoicedetail/delete/<int:pk>', views.InvoiceDetailDestroyAPIView().as_view(), name='invoicedetail_delete'),

    path('nightaudits', views.BookingNightAuditByDateListAPIView().as_view(), name='nightaudits'),
    path('nightaudit_commit/<int:pk>', views.NightAuditCommitUpdateAPIView().as_view(), name='nightauditcommit'),
    path('guestlegers', views.GuestLegerListAPIView().as_view(), name='guestlegers'),

    path('booking/update_status_noshow/<int:pk>', views.PostNoShowUpdateAPIView().as_view(), name='update_status_noshow'),
    path('booking/update_status_noshow_postcharge/<int:pk>', views.PostNoShowRoomChargeUpdateAPIView().as_view(),
         name='update_status_noshow_postcharge'),

    path('person_username', views.PersonByUsernameRetrieveAPIView().as_view(), name='user_retrievebysername'),
    path('person/create', views.PersonCreateCreateAPIView().as_view(), name='person_create'),
    path('person/update/<int:pk>', views.PersonUpdateProfileUpdateAPIView().as_view(), name='person_update'),
    path('person_profile/<int:pk>', views.PersonByIDRetrieveAPIView().as_view(), name='person_editor'),


    path('report/pending_checkin', views.PendingCheckinListAPIView().as_view(), name='pending_checkin'),
    path('report/pending_checkout', views.PendingCheckoutListAPIView().as_view(), name='pending_checkout'),
    path('report/in_house', views.InHouseListAPIView().as_view(), name='in_house'),
    path('report/breakfast', views.BreakfastListAPIView().as_view(), name='breakfast'),

]
