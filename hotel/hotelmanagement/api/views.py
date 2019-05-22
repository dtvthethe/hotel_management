from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password

from hotelmanagement.models import RoomType, Booking, Room, Client, Guest, Product, ProductType, \
    BookingPayment, PaymentType, Config, RoomStatus, Invoice, InvoiceDetail, Person
from django.contrib.auth.models import User, Permission
from .serializers import RoomListSerializer, RoomTypeListSerializer, GuestListSerializer, GuestBookingListSerializer, \
    GuestCreateSerializer, BookingCreateSerializer, ClientListSerializer, GuestBookingDetailSerializer, \
    BookingUpdateSerializer, BookingDeleteSerializer, ProductListSerializer, \
    ProducTypeListSerializer, BookingPaymentSerializer, \
    PaymentTypeListSerializer, BookingPaymentCreateSerializer, \
    BookingPaymentUpdateSerializer, ConfigSerializer, BookingListSerializer, BookingFolioUpdateSerializer, \
    BookingUpdateCheckinSerializer, \
    BookingUpdateCheckoutSerializer, BookingNotInDateRoomListSerializer, UserSerializer, UserCreateSerializer, \
    UserUpdateSerializer, UserChangePasswordSerializer, UserDeleteSerializer, UserPermissionSerializer, \
    Product2ListSerializer, RoomList2Serializer, RoomTypeNoneRefoneListSerializer, RoomTypeDeleteSerializer, \
    ProductTypeCreateSerializer, ProductTypeDeleteSerializer, ProductCreateSerializer, ProductDeleteSerializer, \
    RoomCreateSerializer, RoomDeleteSerializer, RoomStatusListSerializer, InvoiceListSerializer, \
    InvoiceDetailListSerializer, InvoiceDetailCreateSerializer, InvoiceDetailUpdateSerializer, \
    InvoiceDetailPriceConfirmUpdateSerializer, InvoiceDetailDeleteSerializer, InvoiceFolioTransferUpdateSerializer, \
    BookingGuestListSerializer, GuestLegerListSerializer, PostNoShowUpdateSerializer, \
    PostNoShowRoomChargeUpdateSerializer, RoomStatusUpdateSerializer, PersonCreateSerializer, \
    PersonByUsernameSerializer, PersonUpdateProfileSerializer, UserUpdateProfileSerializer, NightAuditCommitSerializer


class Product2ListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = Product2ListSerializer


class Room2ListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomList2Serializer


class Room2TypeListAPIView(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeNoneRefoneListSerializer


class ConfigListAPIView(ListAPIView):
    queryset = Config.objects.all()
    serializer_class = ConfigSerializer


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer


# http://127.0.0.1:8000/api/guest?arrive_date=2019-03-03&depart_date=2019-03-12
class GuestBookingListAPIView(ListAPIView):
    serializer_class = GuestListSerializer

    def get_queryset(self):
        queryset = []
        arrive_date = self.request.query_params.get('arrive_date', None)
        depart_date = self.request.query_params.get('depart_date', None)
        if arrive_date is not None and depart_date is not None:
            queryset1 = Guest.objects.all().filter(Q(booking__arrive_date__range=[arrive_date, depart_date]) and Q(
                booking__depart_date__range=[arrive_date, depart_date]))
            queryset2 = Guest.objects.all().filter(booking__arrive_date__lte=arrive_date).filter(
                booking__depart_date__gte=depart_date)
            queryset3 = Guest.objects.all().filter(
                Q(booking__arrive_date__lt=arrive_date) and Q(booking__arrive_date__lt=depart_date)).filter(
                booking__depart_date__gte=depart_date)
            queryset = queryset1 | queryset2 | queryset3
        return queryset


class RoomRoomTypesListAPIView(ListAPIView):
    serializer_class = RoomTypeListSerializer
    queryset = RoomType.objects.all()


class GuestBookingFOListAPIView(ListAPIView):
    serializer_class = GuestBookingListSerializer

    def get_queryset(self):
        data_value = self.request.query_params.get('data_value', None)
        queryset = []
        if data_value is not None:
            queryset = Guest.objects.all().filter(booking__arrive_date__lte=data_value).filter(
                booking__depart_date__gte=data_value).filter(~Q(booking__booking_status__in=[3,4,5]))
        return queryset


class ClientListAPIView(ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


class ProductTypesListAPIView(ListAPIView):
    serializer_class = ProducTypeListSerializer
    queryset = ProductType.objects.all()


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    queryset = Product.objects.all()


class BookingPaymentListAPIView(ListAPIView):
    serializer_class = BookingPaymentSerializer
    queryset = None

    def get_queryset(self):
        invoice_id = self.request.query_params.get('booking_id', None)
        if invoice_id is not None:
            queryset = BookingPayment.objects.all().filter(booking_id=invoice_id)
        return queryset


class BookingByFolioListAPIView(ListAPIView):
    serializer_class = BookingListSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        if booking_id is not None:
            queryset = Booking.objects.filter(
                Q(booking_folio_transfer_roomcharge=booking_id) | Q(booking_folio_transfer_minibarcharge=booking_id))
        return queryset


class BookingDateNotAvailableListAPIView(ListAPIView):
    serializer_class = BookingNotInDateRoomListSerializer

    def get_queryset(self):
        type = self.request.query_params.get('type', None)
        if type and type == 'new':
            date_start = self.request.query_params.get('date_start', None)
            date_stop = self.request.query_params.get('date_stop', None)
            id_room = self.request.query_params.get('id_room', None)
            if id_room:  # return dates available
                return Booking.objects.filter(room=id_room, booking_status__in=(1, 2))
            elif date_start and date_stop:  # return room
                query_left = Booking.objects.filter(booking_status__in=(1, 2), arrive_date__lte=date_start,
                                                    depart_date__lte=date_stop)
                query_right = Booking.objects.filter(booking_status__in=(1, 2), arrive_date__gte=date_start,
                                                     depart_date__gte=date_stop)
                join_all = query_left | query_right
                return join_all
            else:
                return None
        elif type and type == 'edit':
            id = self.request.query_params.get('type', None)
            return Booking.objects.all()
        else:
            return None


class UserListAPIView(ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()


class PaymentTypeListAPIView(ListAPIView):
    serializer_class = PaymentTypeListSerializer
    queryset = PaymentType.objects.all()


class UserPermissionListAPIView(ListAPIView):
    serializer_class = UserPermissionSerializer
    queryset = Permission.objects.all()


class RoomStatusListAPIView(ListAPIView):
    serializer_class = RoomStatusListSerializer
    queryset = RoomStatus.objects.all()


class InvoiceListAPIView(ListAPIView):
    serializer_class = InvoiceListSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        guest_id = self.request.query_params.get('guest_id', None)
        invoice_id = self.request.query_params.get('invoice_id', None)
        if invoice_id is None:
            invoice_q = Invoice.objects.filter(booking_id=booking_id, guest_id=guest_id)[0]
            # ref_invoice = Invoice.objects.filter(folio_transfer_roomcharge = invoice_q.pk, )
            invoice_id = invoice_q.pk

        invoices = Invoice.objects.filter(pk=invoice_id) | \
        Invoice.objects.filter(Q(folio_transfer_minibarcharge=invoice_id) | Q(folio_transfer_roomcharge=invoice_id))

        # invoices = (Invoice.objects.filter(pk=invoice_id) | \
        # Invoice.objects.filter(Q(folio_transfer_minibarcharge=invoice_id), Q(folio_transfer_roomcharge=None, invoices__product__exact=1)) | \
        # Invoice.objects.filter(Q(folio_transfer_minibarcharge = None), Q(folio_transfer_roomcharge=invoice_id, invoices__product=1 )) | \
        # Invoice.objects.filter(Q(folio_transfer_minibarcharge = invoice_id, folio_transfer_roomcharge=invoice_id))).distinct()
        return invoices


class BookingNightAuditByDateListAPIView(ListAPIView):
    serializer_class = BookingGuestListSerializer
    queryset = None

    def get_queryset(self):
        arrive_date = self.request.query_params.get('arrive_date', None)
        depart_date = self.request.query_params.get('depart_date', None)
        if arrive_date is not None:
            return Booking.objects.filter(arrive_date = arrive_date)
        else:
            return Booking.objects.filter(depart_date = depart_date)


class GuestLegerListAPIView(ListAPIView):
    serializer_class = GuestLegerListSerializer
    queryset = None

    def get_queryset(self):
        arrive_date = self.request.query_params.get('arrive_date', None)
        depart_date = self.request.query_params.get('depart_date', None)
        booking_id = self.request.query_params.get('booking_id', None)
        fullname = self.request.query_params.get('fullname', None)
        client = self.request.query_params.get('client', None)

        queryset = Booking.objects
        if arrive_date is not None and depart_date is not None:
            queryset = queryset.filter(arrive_date__gte=arrive_date).filter(depart_date__lte=depart_date)
        if booking_id is not None:
            queryset = queryset.filter(booking_code=booking_id)
        if fullname is not None:
            queryset = queryset.filter(guests__fullname__contains=fullname)
        if client is not None:
            if client == '0':
                queryset = queryset.all()
            else:
                queryset = queryset.filter(client=client)
        return queryset


class PendingCheckinListAPIView(ListAPIView):
    serializer_class = GuestListSerializer
    queryset = None
    def get_queryset(self):
        query = self.request.query_params.get('arrive_date', None)
        return Guest.objects.all().filter(booking__booking_status_id=1).filter(booking__arrive_date=query)

class PendingCheckoutListAPIView(ListAPIView):
    serializer_class = GuestListSerializer
    queryset = None
    def get_queryset(self):
        query = self.request.query_params.get('depart_date', None)
        return Guest.objects.all().filter(booking__booking_status_id=2).filter(booking__depart_date=query)

class InHouseListAPIView(ListAPIView):
    serializer_class = GuestListSerializer
    queryset = Guest.objects.all().filter(booking__booking_status_id=2)


class BreakfastListAPIView(ListAPIView):
    serializer_class = GuestListSerializer
    queryset = None

    def get_queryset(self):
        query = self.request.query_params.get('q_date', None)
        return Guest.objects.all().filter(booking__arrive_date__lte=query) \
        .filter(booking__depart_date__gte=query). \
        filter(~Q(booking__booking_status__in=[1, 3, 4, 5])).filter(booking__is_breakfast=True)



# Create:
class RoomCreateAPIView(CreateAPIView):
    serializer_class = RoomCreateSerializer


class ProductCreateAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer


class RoomTypeCreateAPIView(CreateAPIView):
    serializer_class = RoomTypeNoneRefoneListSerializer


class ProductTypeCreateAPIView(CreateAPIView):
    serializer_class = ProductTypeCreateSerializer


class UserCreateAPIView(APIView):
    serializer_class = UserCreateSerializer

    def post(self, request):
        validate_password(request.data['password'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()

            return Response(serializer.data)
        else:
            return Response({'message': True})


class GuestCreateAPIView(CreateAPIView):
    serializer_class = GuestCreateSerializer


class BokingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        Guest.objects.create(fullname=self.request.data['guest']['fullname'], booking_id=booking.pk)


class BookingPaymentCreateAPIView(CreateAPIView):
    serializer_class = BookingPaymentCreateSerializer


class InvoiceDetailCreateAPIView(CreateAPIView):
    serializer_class = InvoiceDetailCreateSerializer

class PersonCreateCreateAPIView(CreateAPIView):
    serializer_class = PersonCreateSerializer

    def post(self, request):
        validate_password(request.data['password'])
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            user.set_password(request.data['password'])
            user.save()

            return Response(serializer.data)
        else:
            return Response({'message': True})



# Retrieve:
class GuestBookingRetrieveAPIView(RetrieveAPIView):
    serializer_class = GuestBookingDetailSerializer
    queryset = Guest.objects.all()


#
# class BookingUpdateFolioTransferAPIView(RetrieveAPIView):
#     serializer_class = GuestBookingDetailSerializer
#     queryset = Guest.objects.all()

class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

# class PersonByUsernameRetrieveAPIView(RetrieveAPIView):
#     serializer_class = PersonByUsernameSerializer
#     queryset = Person.objects.all()
#
#     # def get_object(self, username):
#     #     try:
#     #         print(username)
#     #         return Person.objects.get(username=username)
#     #     except BaseException as ex:
#     #         return Response(ex)


class PersonByUsernameRetrieveAPIView(ListAPIView):
    serializer_class = PersonByUsernameSerializer
    queryset = None

    def get_queryset(self):
        str_username = self.request.query_params.get('username', None)
        if str_username is not None:
            return User.objects.filter(username=str_username)
        else:
            raise Http404({'asa': 'afw'})

class PersonByIDRetrieveAPIView(RetrieveAPIView):
    serializer_class = PersonUpdateProfileSerializer
    queryset = Person.objects.all()



# Update:
class RoomUpdateAPIView(UpdateAPIView):
    serializer_class = RoomCreateSerializer
    queryset = Room.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    serializer_class = ProductCreateSerializer
    queryset = Product.objects.all()


class ProductTypeUpdateAPIView(UpdateAPIView):
    serializer_class = ProductTypeCreateSerializer
    queryset = ProductType.objects.all()


class RoomTypeUpdateAPIView(UpdateAPIView):
    serializer_class = RoomTypeNoneRefoneListSerializer
    queryset = RoomType.objects.all()


class UserUpdateAPIView(UpdateAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()


class UserPasswordUpdateAPIView(APIView):
    serializer_class = UserChangePasswordSerializer
    queryset = User.objects.all()

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except BaseException as ex:
            return Response(ex)

    def put(self, request, pk, format=None):
        user = self.get_object(pk)
        serializer = self.serializer_class(user, request.data)
        validate_password(request.data['password'])
        if serializer.is_valid():
            serializer.save()
            user.set_password(serializer.data.get('password'))
            user.save()
            return Response(serializer.data)
        return Response({'message': True})


class BookingUpdateAPIView(UpdateAPIView):
    serializer_class = BookingUpdateSerializer
    queryset = Booking.objects.all()


class ReverationUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()
        guest = self.request.data['guest']
        Guest.objects.filter(pk=self.request.data['guest']['id']).update(fullname=guest['fullname'])


class BookingPaymentUpdateAPIView(UpdateAPIView):
    queryset = BookingPayment.objects.all()
    serializer_class = BookingPaymentUpdateSerializer


# class BookingCheckInUpdateAPIView(UpdateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingUpdateCheckinSerializer
#     def perform_update(self, serializer):
#         booking_save = serializer.save()
#         guest_booking = Guest.objects.get(booking_id=booking_save.pk)
#         if not Invoice.objects.filter(booking_id=booking_save.pk, guest=guest_booking.pk).exists():
#             result = Invoice.objects.create(booking_id=booking_save.pk, guest_id=guest_booking.pk)


class NightAuditCommitUpdateAPIView(UpdateAPIView):
    serializer_class = NightAuditCommitSerializer
    queryset = Config.objects.all()

class CheckInAPIView(APIView):  # parameter is booking ID
    serializer_class = InvoiceListSerializer
    queryset = None

    def get_object(self, pk, guest_id):
        try:
            return Invoice.objects.filter(booking_id=pk, guest_id=guest_id)
        except BaseException as ex:
            return Response(ex)

    def put(self, request, pk, format=None):
        # update status booking:
        Booking.objects.filter(pk=pk).update(booking_status=request.data['booking_status'])
        # insert to invoice:
        if not Invoice.objects.filter(booking_id=pk, guest=request.data['guest_id']).exists():
            inv = Invoice.objects.create(booking_id=request.data['booking_id'], guest_id=request.data['booking_id'])
            serializer = self.serializer_class(inv)
            return Response(serializer.data['id'])
        return Response({'message': True})


class BookingCheckOutUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateCheckoutSerializer

    def perform_update(self, serializer):
        booking = serializer.save()
        Room.objects.filter(pk=booking.room.pk).update(room_status=1)


class InvoiceDetailUpdateAPIView(UpdateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailUpdateSerializer


class InvoiceDetailPriceConfirmUpdateAPIView(UpdateAPIView):
    queryset = InvoiceDetail.objects.all()
    serializer_class = InvoiceDetailPriceConfirmUpdateSerializer


class InvoiceFolioUpdateAPIView(UpdateAPIView):
    queryset = Invoice.objects.all()
    serializer_class = InvoiceFolioTransferUpdateSerializer

    def perform_update(self, serializer):
        param_data = self.request.data
        if (param_data['folio_transfer_minibarcharge'] == None and param_data['folio_transfer_roomcharge'] == None):
            serializer.save()
        else:
            invoice_id = param_data['folio_transfer_minibarcharge']
            if invoice_id == None:
                invoice_id = param_data['folio_transfer_roomcharge']
            invoice = Invoice.objects.get(pk=invoice_id)
            if (invoice.folio_transfer_minibarcharge == None and invoice.folio_transfer_roomcharge == None):
                serializer.save()
            else:
                serializer.data['folio_transfer_minibarcharge'] = -1
                serializer.data['folio_transfer_roomcharge'] = -1

                raise Http404({'asa': 'afw'})

class PostNoShowUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = PostNoShowUpdateSerializer


class PostNoShowRoomChargeUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = PostNoShowRoomChargeUpdateSerializer

    def perform_update(self, serializer):
        date_session = self.request.data['date_session']
        price_confirm = self.request.data['price_confirm']
        if (date_session is not None and price_confirm is not None):
            bk = serializer.save()
            guest = Guest.objects.get(booking_id=bk.pk)
            a = 1
            inv = Invoice.objects.create(booking_id=bk.pk, guest_id=guest.pk)
            InvoiceDetail.objects.create(price_confirm=price_confirm, quantity= 1, date_session=date_session, invoice_id= inv.pk, product_id=1)
        else:
            raise Http404({'asa': 'afw'})

class RoomStatusUpdateAPIView(UpdateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomStatusUpdateSerializer


# class PersonUpdateProfileUpdateAPIView(UpdateAPIView):
#     queryset = Person.objects.all()
#     serializer_class = PersonUpdateProfileSerializer
#
#     def perform_update(self, serializer):
#         avatar = self.request.data['avatar']
#         if(avatar is not None):
#             serializer.save()
#         else:
#             serializer.save()

class PersonUpdateProfileUpdateAPIView(UpdateAPIView):
    queryset = Person.objects.all()
    serializer_class = UserUpdateProfileSerializer

# Delete:
class RoomDestroyAPIView(DestroyAPIView):
    serializer_class = RoomDeleteSerializer
    queryset = Room.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    serializer_class = ProductDeleteSerializer
    queryset = Product.objects.all()


class ProductTypeDestroyAPIView(DestroyAPIView):
    serializer_class = ProductTypeDeleteSerializer
    queryset = ProductType.objects.all()


class RoomTypeDestroyAPIView(DestroyAPIView):
    serializer_class = RoomTypeDeleteSerializer
    queryset = RoomType.objects.all()


class BookingDestroyAPIView(DestroyAPIView):
    serializer_class = BookingDeleteSerializer
    queryset = Booking.objects.all()


class BookingPaymentDestroyAPIView(DestroyAPIView):
    serializer_class = BookingPaymentSerializer
    queryset = BookingPayment.objects.all()


class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserDeleteSerializer
    queryset = User.objects.all()


class InvoiceDetailDestroyAPIView(DestroyAPIView):
    serializer_class = InvoiceDetailDeleteSerializer
    queryset = InvoiceDetail.objects.all()


