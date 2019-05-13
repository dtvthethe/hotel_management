from django.contrib import admin
from .models import Booking,PaymentType, Product, RoomStatus, RoomType, Client, BookingPayment, Guest, ProductType, Room, \
    Invoice, InvoiceDetail, Person

# Register your models here.

admin.site.register(Booking)
admin.site.register(PaymentType)
admin.site.register(RoomStatus)
admin.site.register(RoomType)
admin.site.register(Client)
admin.site.register(BookingPayment)
admin.site.register(Guest)
admin.site.register(Invoice)
admin.site.register(ProductType)
admin.site.register(Room)
admin.site.register(InvoiceDetail)
admin.site.register(Product)
admin.site.register(Person)