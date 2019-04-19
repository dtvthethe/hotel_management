from django.db import models
from django.utils import timezone

# Init data: https://code.djangoproject.com/wiki/Fixtures

# phase 1.
class Config(models.Model):
    name = models.CharField(max_length=20, unique=True)
    session_date = models.DateField()

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class RoomType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class PaymentType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BookingStatus(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# phase 2
class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.ForeignKey(RoomType, related_name='rooms', on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)
    room_status = models.ForeignKey(RoomStatus, related_name='room_list', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product_type = models.ForeignKey(ProductType, related_name='products', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

#phase 3
class Booking(models.Model):
    booking_code = models.CharField(max_length=20)
    adult = models.IntegerField(default=0)
    child = models.IntegerField(default=0)
    note = models.TextField()
    arrive_date = models.DateField()
    depart_date = models.DateField()
    is_breakfast = models.BooleanField(default=True)
    price_booking = models.IntegerField(default=0)
    client = models.ForeignKey(Client, related_name='booking_clients', on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='booking_room', on_delete=models.CASCADE)
    booking_status = models.ForeignKey(BookingStatus, related_name= 'status', on_delete=models.CASCADE)
    booking_folio_transfer_roomcharge = models.ForeignKey('self', default=None, null= True, on_delete=models.SET_NULL, related_name='bk_folio_transfer_roomcharge')
    booking_folio_transfer_minibarcharge = models.ForeignKey('self', default=None, null= True, on_delete=models.SET_NULL, related_name='bk_folio_transfer_minibarcharge')

    def __str__(self):
        return self.booking_code

#phase 4
class Guest(models.Model):
    fullname = models.CharField(max_length=150)
    booking = models.ForeignKey(Booking, related_name='guests', on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

class MinibarCharge(models.Model):
    price_confirm = models.IntegerField(default=0)
    quantity = models.IntegerField(default=0)
    date_order = models.DateTimeField(default=timezone.now)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_order

class RoomCharge(models.Model):
    price_confirm = models.IntegerField(default=0)
    date_charge = models.DateTimeField(default=timezone.now)
    date_session = models.DateField()
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_charge

#phase 5
class BookingPayment(models.Model):
    credit = models.IntegerField(default=0)
    date_pay = models.DateTimeField(default=timezone.now)
    desciption = models.CharField(max_length=200)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)

    def __str__(self):
        return self.date_pay