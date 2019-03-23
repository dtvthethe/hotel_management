from django.db.models import Q
from rest_framework.generics import ListAPIView
from hotelmanagement.models import RoomType, RoomStatus, Room, Booking, Guest
from .serializers import RoomListSerializer, BookingListSerializer, GuestListSerializer


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer


# http://127.0.0.1:8000/api/booking?arrive_date=2019-03-03&depart_date=2019-03-12
class BookingListAPIView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = BookingListSerializer

    def get_queryset(self):
        queryset = Booking.objects.all()
        arrive_date = self.request.query_params.get('arrive_date', None)
        depart_date = self.request.query_params.get('depart_date', None)
        if arrive_date is not None or depart_date is not None:
            queryset = queryset.select_related('client').filter(arrive_date__gte=arrive_date).filter(
                depart_date__lte=depart_date)
        return queryset

#http://127.0.0.1:8000/api/guest?arrive_date=2019-03-03&depart_date=2019-03-12
class GuestBookingListAPIView(ListAPIView):
    serializer_class = GuestListSerializer

    def get_queryset(self):
        queryset = []
        arrive_date = self.request.query_params.get('arrive_date', None)
        depart_date = self.request.query_params.get('depart_date', None)
        if arrive_date is not None and depart_date is not None:
            queryset1 = Guest.objects.all().filter(booking__arrive_date__range=[arrive_date, depart_date])
            queryset2 = Guest.objects.all().filter(booking__arrive_date__lt=arrive_date).filter(booking__depart_date__gt=depart_date)
            queryset = queryset1 | queryset2
            # queryset = Guest.objects.all().filter(Q(booking__arrive_date__in=[arrive_date, depart_date]) and Q(booking__depart_date__in=[arrive_date, depart_date]))
            #or Q(booking__arrive_date__lte=arrive_date))
        return queryset
