from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.hashers import check_password, make_password
from django.contrib.auth.password_validation import validate_password

from hotelmanagement.models import RoomType, Booking, Room, Client, Guest, Product, ProductType, MinibarCharge, \
    BookingPayment, RoomCharge, PaymentType, Config, RoomStatus
from django.contrib.auth.models import User, Permission
from .serializers import RoomListSerializer, RoomTypeListSerializer, GuestListSerializer, GuestBookingListSerializer, \
    GuestCreateSerializer, BookingCreateSerializer, ClientListSerializer, GuestBookingDetailSerializer, \
    MinibarChargeUpdateSerializer, BookingUpdateSerializer, BookingDeleteSerializer, ProductListSerializer, \
    ProducTypeListSerializer, MinibarChargeSerializer, BookingPaymentSerializer, RoomChargeSerializer, \
    MinibarChargeCreateSerializer, PaymentTypeListSerializer, BookingPaymentCreateSerializer, \
    BookingPaymentUpdateSerializer, ConfigSerializer, BookingListSerializer, BookingFolioUpdateSerializer, \
    RoomChargeByBookingListSerializer, MiniBarChargeByBookingListSerializer, BookingUpdateCheckinSerializer, \
    BookingUpdateCheckoutSerializer, BookingNotInDateRoomListSerializer, UserSerializer, UserCreateSerializer, \
    UserUpdateSerializer, UserChangePasswordSerializer, UserDeleteSerializer, UserPermissionSerializer, \
    Product2ListSerializer, RoomList2Serializer, RoomTypeNoneRefoneListSerializer, RoomTypeDeleteSerializer, \
    ProductTypeCreateSerializer, ProductTypeDeleteSerializer, ProductCreateSerializer, ProductDeleteSerializer, \
    RoomCreateSerializer, RoomDeleteSerializer, RoomStatusListSerializer, RoomChargeRoomRateSerializer


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
        session_date = self.request.query_params.get('session_date', None)
        queryset = []
        if session_date is not None:
            # queryset = Booking.objects.all().filter(arrive_date__lte=session_date).filter(depart_date__gte=session_date)
            queryset = Guest.objects.all().filter(booking__arrive_date__lte=session_date).filter(
                booking__depart_date__gte=session_date).filter(~Q(booking__booking_status=3))
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


class MinibarChargeListAPIView(ListAPIView):
    serializer_class = MinibarChargeSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        if booking_id is not None:
            queryset = MinibarCharge.objects.all().filter(booking_id=booking_id)
        return queryset


class BookingPaymentListAPIView(ListAPIView):
    serializer_class = BookingPaymentSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        if booking_id is not None:
            queryset = BookingPayment.objects.all().filter(booking_id=booking_id)
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


# http://127.0.0.1:8000/roomcharge?booking_id=1
class RoomChargeListAPIView(ListAPIView):
    serializer_class = RoomChargeByBookingListSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        if booking_id is not None:
            booking_ids = Booking.objects.filter(booking_folio_transfer_roomcharge=booking_id).values_list('id',
                                                                                                           flat=True)
            queryset = RoomCharge.objects.filter(booking_id__in=booking_ids) | RoomCharge.objects.all().filter(
                booking_id=booking_id)
        return queryset


# http://127.0.0.1:8000/minibarchargebybooking?booking_id=1
class MinibarChargeByBookingListAPIView(ListAPIView):
    serializer_class = MiniBarChargeByBookingListSerializer
    queryset = None

    def get_queryset(self):
        booking_id = self.request.query_params.get('booking_id', None)
        if booking_id is not None:
            booking_ids = Booking.objects.filter(booking_folio_transfer_minibarcharge=booking_id).values_list('id',
                                                                                                              flat=True)
            queryset = MinibarCharge.objects.filter(booking_id__in=booking_ids) | MinibarCharge.objects.all().filter(
                booking_id=booking_id)
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
                a = Booking.objects.filter(booking_status__in=(1, 2), arrive_date__lte=date_start, depart_date__lte=date_stop)
                b = Booking.objects.filter(booking_status__in=(1, 2), arrive_date__gte=date_start, depart_date__gte=date_stop)
                c = a | b
                return c
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


class MinibarChargeCreateAPIView(CreateAPIView):
    serializer_class = MinibarChargeCreateSerializer


class BookingPaymentCreateAPIView(CreateAPIView):
    serializer_class = BookingPaymentCreateSerializer


class RoomChargeCreateAPIView(CreateAPIView):
    serializer_class = RoomChargeSerializer


# Retrieve:
class GuestBookingRetrieveAPIView(RetrieveAPIView):
    serializer_class = GuestBookingDetailSerializer
    queryset = Guest.objects.all()


class MinibarChargeRetrieveAPIView(RetrieveAPIView):
    serializer_class = MinibarChargeSerializer
    queryset = MinibarCharge.objects.all()


class BookingUpdateFolioTransferAPIView(RetrieveAPIView):
    serializer_class = GuestBookingDetailSerializer
    queryset = Guest.objects.all()

class UserRetrieveAPIView(RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

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


    # def perform_update(self, serializer: UserSerializer):
    #     password = serializer.validated_data.pop('password', None)
    #     a = pk
    #     if password is not None:
    #         c = self.queryset
    #         validate_password(password)
    #         pw = make_password(password)
    #         # serializer.
    #         User.objects.update(password = password)
    #
    #     c = 1


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


class MinibarChargeUpdateAPIView(UpdateAPIView):
    queryset = MinibarCharge.objects.all()
    serializer_class = MinibarChargeUpdateSerializer


class BookingPaymentUpdateAPIView(UpdateAPIView):
    queryset = BookingPayment.objects.all()
    serializer_class = BookingPaymentUpdateSerializer


class BookingCheckInUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateCheckinSerializer


class BookingCheckOutUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateCheckoutSerializer

    def perform_update(self, serializer):
        booking = serializer.save()
        Room.objects.filter(pk=booking.room.pk).update(room_status=1)


class RoomChargeUpdateAPIView(UpdateAPIView):
    queryset = RoomCharge.objects.all()
    serializer_class = RoomChargeSerializer

class RoomChargeRateRoomUpdateAPIView(UpdateAPIView):
    queryset = RoomCharge.objects.all()
    serializer_class = RoomChargeRoomRateSerializer


class BookingFolioUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingFolioUpdateSerializer


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


class MinibarChargeDestroyAPIView(DestroyAPIView):
    serializer_class = MinibarChargeSerializer
    queryset = MinibarCharge.objects.all()


class BookingPaymentDestroyAPIView(DestroyAPIView):
    serializer_class = BookingPaymentSerializer
    queryset = BookingPayment.objects.all()


class RoomChargeDestroyAPIView(DestroyAPIView):
    serializer_class = RoomChargeSerializer
    queryset = RoomCharge.objects.all()

class UserDestroyAPIView(DestroyAPIView):
    serializer_class = UserDeleteSerializer
    queryset = User.objects.all()


#
# class BookingAPIView(APIView):
#     def get_object(self, pk):
#         try:
#             return Booking.objects.get(pk=pk)
#         except Booking.DoesNotExist:
#             raise Http404
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = BookingFolioUpdateSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
