from django.db.models import Q
from rest_framework.generics import ListAPIView
from hotelmanagement.models import RoomType, RoomStatus, Room
from .serializers import RoomListSerializer

class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomListSerializer