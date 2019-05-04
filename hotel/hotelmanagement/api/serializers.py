from rest_framework.serializers import ModelSerializer
from hotelmanagement.models import Room, Booking, Guest, RoomStatus, Client, ProductType, Product, \
    BookingPayment, RoomType, PaymentType, BookingStatus, Config, Invoice, InvoiceDetail
from django.contrib.auth.models import User, Permission

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        # fields = ('id', 'last_login', 'is_superuser', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active','groups', 'user_permissions' )
        fields = '__all__'

class UserPermissionSerializer(ModelSerializer):
    class Meta:
        model = Permission
        fields = ('id', 'codename', 'name' )


class ConfigSerializer(ModelSerializer):
    class Meta:
        model = Config
        fields = '__all__'

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
    room_status = RoomStatusListSerializer(many = False)
    class Meta:
        model = Room
        fields = '__all__'


class ProductListSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class BookingStatusListSerializer(ModelSerializer):
    class Meta:
        model = BookingStatus
        fields = '__all__'

class BookingListSerializer(ModelSerializer):
    booking_status = BookingStatusListSerializer(many=False)
    class Meta:
        model = Booking
        fields = '__all__'

class BookingNotInDateRoomListSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ('id', 'arrive_date', 'depart_date', 'room')

class BookingCalendarListSerializer(ModelSerializer):
    client = ClientListSerializer(many = False)
    room = RoomListSerializer(many= False)
    booking_status = BookingStatusListSerializer(many=False)
    class Meta:
        model = Booking
        fields = '__all__'


class GuestListSerializer(ModelSerializer):
    booking = BookingCalendarListSerializer(many = False)
    class Meta:
        model = Guest
        fields = '__all__'

class BookingGuestListSerializer(ModelSerializer):
    booking_status = BookingStatusListSerializer(many=False)
    room = RoomListSerializer(many=False)
    guests = GuestListSerializer(many=True)
    class Meta:
        model = Booking
        fields = '__all__'

class GuestLegerListSerializer(ModelSerializer):
    booking_status = BookingStatusListSerializer(many=False)
    room = RoomListSerializer(many=False)
    guests = GuestListSerializer(many=True)
    client = ClientListSerializer(many=False)

    class Meta:
        model = Booking
        fields = '__all__'


class GuestBookingListSerializer(ModelSerializer):
    booking = BookingListSerializer(many = False)
    class Meta:
        model = Guest
        fields = '__all__'


class BookingPaymentSerializer(ModelSerializer):
    payment_type = PaymentTypeListSerializer(many=False)
    class Meta:
        model = BookingPayment
        fields = '__all__'


class RoomTypeListSerializer(ModelSerializer):
    rooms = RoomListSerializer(many=True)
    class Meta:
        model = RoomType
        fields = '__all__'



class RoomTypeNoneRefoneListSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class BookingByRoomChageListSerializer(ModelSerializer):
    room = RoomListSerializer(many = False)
    class Meta:
        model = Booking
        fields = '__all__'

class BookingByMiniBarListSerializer(ModelSerializer):
    room = RoomListSerializer(many = False)
    class Meta:
        model = Booking
        fields = '__all__'

class RoomList2Serializer(ModelSerializer):
    room_status = RoomStatusListSerializer(many=False)
    room_type = RoomTypeNoneRefoneListSerializer(many=False)
    class Meta:
        model = Room
        fields = '__all__'

class BookingInvoiceListSerializer(ModelSerializer):
    room = RoomListSerializer(many=False)
    class Meta:
        model = Booking
        fields = '__all__'

class Product2ListSerializer(ModelSerializer):
    product_type = ProducTypeListSerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'

class InvoiceDetail1ListSerializer(ModelSerializer):
    product = ProductListSerializer(many=False)
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

class InvoiceListSerializer(ModelSerializer):
    guest = GuestListSerializer(many=False)
    booking = BookingInvoiceListSerializer(many=False)
    invoices = InvoiceDetail1ListSerializer(many=True)
    class Meta:
        model = Invoice
        fields = '__all__'

class InvoiceDetailListSerializer(ModelSerializer):
    invoice = InvoiceListSerializer(many=False)
    product = ProductListSerializer(many=False)
    class Meta:
        model = InvoiceDetail
        fields = '__all__'


# Create:

class GuestCreateSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class BookingCreateSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingPaymentCreateSerializer(ModelSerializer):
    class Meta:
        model = BookingPayment
        fields = '__all__'

class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RoomCreateSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class ProductTypeCreateSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class InvoiceDetailCreateSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = '__all__'

# Retrieve:
class BookingDetailSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class GuestBookingDetailSerializer(ModelSerializer):
    booking = BookingDetailSerializer(many = False)
    class Meta:
        model = Guest
        fields = '__all__'

# Update

class GuestUpdateSerializer(ModelSerializer):
    class Meta:
        model = Guest
        fields = '__all__'

class BookingUpdateSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class BookingUpdateCheckinSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_status']

class BookingUpdateCheckoutSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ['booking_status']

class BookingFolioUpdateSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = ('booking_folio_transfer_roomcharge', 'booking_folio_transfer_minibarcharge')


class BookingPaymentUpdateSerializer(ModelSerializer):
    class Meta:
        model = BookingPayment
        fields = '__all__'

class UserUpdateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('is_superuser', 'first_name', 'last_name', 'email', 'is_staff', 'is_active','groups', 'user_permissions' )

class UserChangePasswordSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ['password']

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class RoomTypeSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = '__all__'

class ProductTypeSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = '__all__'

class InvoiceDetailPriceConfirmUpdateSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['price_confirm']

class InvoiceDetailUpdateSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['product', 'price_confirm', 'quantity']



class InvoiceFolioTransferUpdateSerializer(ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['folio_transfer_roomcharge', 'folio_transfer_minibarcharge']

# Delete
class BookingDeleteSerializer(ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'


class UserDeleteSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ProductDeleteSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id']

class ProductTypeDeleteSerializer(ModelSerializer):
    class Meta:
        model = ProductType
        fields = ['id']

class RoomTypeDeleteSerializer(ModelSerializer):
    class Meta:
        model = RoomType
        fields = ['id']

class RoomDeleteSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ['id']

class InvoiceDetailDeleteSerializer(ModelSerializer):
    class Meta:
        model = InvoiceDetail
        fields = ['id']