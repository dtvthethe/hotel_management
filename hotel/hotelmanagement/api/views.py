from django.db.models import Q
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from hotelmanagement.models import RoomType, Booking, Room, Client, Guest
from .serializers import RoomListSerializer, RoomTypeListSerializer, GuestListSerializer, GuestBookingListSerializer, \
    GuestCreateSerializer, BookingCreateSerializer, ClientListSerializer, GuestBookingDetailSerializer, \
    GuestUpdateSerializer, BookingUpdateSerializer, BookingDeleteSerializer


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
                booking__depart_date__gte=session_date)
        return queryset

class ClientListAPIView(ListAPIView):
    serializer_class = ClientListSerializer
    queryset = Client.objects.all()


# Create:

class GuestCreateAPIView(CreateAPIView):
    serializer_class = GuestCreateSerializer



class BokingCreateAPIView(CreateAPIView):
    serializer_class = BookingCreateSerializer

    def perform_create(self, serializer):
        booking = serializer.save()
        Guest.objects.create(fullname=self.request.data['guest']['fullname'], booking_id=booking.pk)

# Retrieve:

class GuestBookingRetrieveAPIView(RetrieveAPIView):
    serializer_class = GuestBookingDetailSerializer
    queryset = Guest.objects.all()

# Update:
# class GuestUpdateAPIView(UpdateAPIView):
#     serializer_class = GuestUpdateSerializer

class ReverationUpdateAPIView(UpdateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingUpdateSerializer

    def perform_update(self, serializer):
        serializer.save()
        guest = self.request.data['guest']
        Guest.objects.filter(pk=self.request.data['guest']['id']).update(fullname = guest['fullname'])

#Delete:
class BookingDestroyAPIView(DestroyAPIView):
    serializer_class = BookingDeleteSerializer
    queryset = Booking.objects.all()

    # def perform_destroy(self, instance):

