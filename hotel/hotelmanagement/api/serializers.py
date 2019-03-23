from rest_framework.serializers import ModelSerializer, PrimaryKeyRelatedField, StringRelatedField
from hotelmanagement.models import Room, Booking, Guest, RoomStatus, Client, ProductType, Product, RoomCharge, MinibarCharge, BookingPayment, RoomType, PaymentType


class ClientListSerializer(ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class RoomStatusListSerializer(ModelSerializer):
    class Meta:
        model = RoomStatus
        fields = '__all__'


class ProducTypeListSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'



class PaymentTypeListSerializer(ModelSerializer):
    class Meta:
        model = PaymentType
        fields = '__all__'


class RoomListSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class BookingListSerializer(ModelSerializer):
    client = ClientListSerializer(many = False)
    room = RoomListSerializer(many= False)
    class Meta:
        model = Booking
        fields = '__all__'

class GuestListSerializer(ModelSerializer):
    booking = BookingListSerializer(many = False)
    class Meta:
        model = Guest
        fields = '__all__'





class MinibarChargeSerializer(ModelSerializer):
    class Meta:
        model = MinibarCharge
        fields = '__all__'


class RoomChargeSerializer(ModelSerializer):
    class Meta:
        model = RoomCharge
        fields = '__all__'


class BookingPaymentSerializer(ModelSerializer):
    class Meta:
        model = BookingPayment
        fields = '__all__'


class RoomTypeListSerializer(ModelSerializer):
    rooms = RoomListSerializer(many=True)
    class Meta:
        model = RoomType
        fields = '__all__'