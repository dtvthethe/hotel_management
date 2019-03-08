from django.db.models import Q
from rest_framework.generics import ListAPIView
from hotelmanagement.models import RoomType, RoomStatus
from .serializers import RoomTypeListSerializer

class RoomListAPIView(ListAPIView):
    queryset = RoomType.objects.all()
    serializer_class = RoomTypeListSerializer