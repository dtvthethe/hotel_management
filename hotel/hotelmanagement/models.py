from django.db import models

# Init data: https://code.djangoproject.com/wiki/Fixtures

# phase 1.

class Client(models.Model):
    name = models.CharField(max_length=100)

class RoomStatus(models.Model):
    name = models.CharField(max_length=100)

class ProductType(models.Model):
    name = models.CharField(max_length=100)

class RoomType(models.Model):
    name = models.CharField(max_length=100)

class PaymentType(models.Model):
    name = models.CharField(max_length=100)

# phase 2
class Room(models.Model):
    name = models.CharField(max_length=100)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    price = models.IntegerField(default=0)
    capacity = models.IntegerField(default=0)

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField(default=0)
    product_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

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
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    room = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)

#phase 4
class Guest(models.Model):
    fullname = models.CharField(max_length=150)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

class MinibarCharge(models.Model):
    quantity = models.IntegerField(default=0)
    date_order = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

class RoomCharge(models.Model):
    price_confirm = models.IntegerField(default=0)
    date_charge = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)

#phase 5
class BookingPayment(models.Model):
    credit = models.IntegerField(default=0)
    date_pay = models.DateTimeField(auto_now_add=True)
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    payment = models.ForeignKey(PaymentType, on_delete=models.CASCADE)