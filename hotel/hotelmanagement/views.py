import datetime

from django.core.paginator import Paginator
from django.db.models import Q, F, Sum, Prefetch
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from rest_framework_jwt.serializers import User

from hotelmanagement.forms import ProductTypeForm, RoomTypeForm, ClientForm, ConfigForm, PaymentTypeForm, ProductForm, \
    RoomForm, PersonForm
from .models import ProductType, RoomType, Client, Config, PaymentType, Product, Room, Person, Invoice, InvoiceDetail, \
    BookingPayment, Booking, Guest


# ProductType

def producttype_list(request):
    lst = ProductType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Product Type List', 'lst': data_rows}
    return render(request, 'producttype/list.html', context=context)


def producttype_create(request):
    try:
        if request.method == 'POST':
            form = ProductTypeForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'producttype/create.html', context={'title': 'New Product Type', 'form': ProductTypeForm()})


def producttype_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(ProductType, id=id)
        form = ProductTypeForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:producttypes')
        context = {
            'title': 'Product Type Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'producttype/edit.html', context=context)


def producttype_delete(request, id=None):
    try:
        instance = get_object_or_404(ProductType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:producttypes')


# RoomType

def roomtype_list(request):
    lst = RoomType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Room Type List', 'lst': data_rows}
    return render(request, 'roomtype/list.html', context=context)


def roomtype_create(request):
    try:
        if request.method == 'POST':
            form = RoomTypeForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'roomtype/create.html', context={'title': 'New Room Type', 'form': RoomTypeForm()})


def roomtype_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(RoomType, id=id)
        form = RoomTypeForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:roomtypes')
        context = {
            'title': 'Room Type Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'roomtype/edit.html', context=context)


def roomtype_delete(request, id=None):
    try:
        instance = get_object_or_404(RoomType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:roomtypes')


# Client

def cient_list(request):
    lst = Client.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Client List', 'lst': data_rows}
    return render(request, 'client/list.html', context=context)


def client_create(request):
    try:
        if request.method == 'POST':
            form = ClientForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'Client/create.html', context={'title': 'New Client', 'form': ClientForm()})


def client_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Client, id=id)
        form = ClientForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:clients')
        context = {
            'title': 'Client Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'client/edit.html', context=context)


def client_delete(request, id=None):
    try:
        instance = get_object_or_404(Client, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:clients')


# Config

def config_list(request):
    lst = Config.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Config List', 'lst': data_rows}
    return render(request, 'config/list.html', context=context)


def config_create(request):
    try:
        if request.method == 'POST':
            form = ConfigForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'config/create.html', context={'title': 'New Config', 'form': ConfigForm()})


def config_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Config, id=id)
        form = ConfigForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:configs')
        context = {
            'title': 'Config Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'config/edit.html', context=context)


def config_delete(request, id=None):
    try:
        instance = get_object_or_404(Config, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:configs')


# Payment Type

def paymenttype_list(request):
    lst = PaymentType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Payment Type List', 'lst': data_rows}
    return render(request, 'paymenttype/list.html', context=context)


def paymenttype_create(request):
    try:
        if request.method == 'POST':
            form = PaymentTypeForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'paymenttype/create.html', context={'title': 'New Payment Type', 'form': PaymentTypeForm()})


def paymenttype_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(PaymentType, id=id)
        form = PaymentTypeForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:paymenttypes')
        context = {
            'title': 'Payment Type Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'paymenttype/edit.html', context=context)


def paymenttype_delete(request, id=None):
    try:
        instance = get_object_or_404(PaymentType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:paymenttypes')


# Product

def product_list(request):
    lst = Product.objects.all()
    query = request.GET.get('q')
    if query:
        lst = lst.filter(Q(name__contains=query) |
                         Q(product_type__name__contains=query)).distinct()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Product List', 'lst': data_rows}
    return render(request, 'product/list.html', context=context)


def product_create(request):
    try:
        if request.method == 'POST':
            form = ProductForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'product/create.html', context={'title': 'New Product', 'form': ProductForm()})


def product_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Product, id=id)
        form = ProductForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:products')
        context = {
            'title': 'Product Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'product/edit.html', context=context)


def product_delete(request, id=None):
    try:
        instance = get_object_or_404(Product, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:products')


# Room

def room_list(request):
    lst = Room.objects.all()
    query = request.GET.get('q')
    if query:
        lst = lst.filter(Q(name__contains=query) |
                         Q(room_status__name__contains=query) |
                         Q(room_type__name__contains=query)).distinct()

    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Room List', 'lst': data_rows}
    return render(request, 'room/list.html', context=context)


def room_create(request):
    try:
        if request.method == 'POST':
            form = RoomForm(request.POST or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'room/create.html', context={'title': 'New Room', 'form': RoomForm()})


def room_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Room, id=id)
        form = RoomForm(request.POST or None, instance=instance)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:rooms')
        context = {
            'title': 'Room Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'room/edit.html', context=context)


def room_delete(request, id=None):
    try:
        instance = get_object_or_404(Room, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:rooms')


# Person

def person_list(request):
    lst = Person.objects.all()
    query = request.GET.get('q')
    # if query:
    #     lst = lst.filter(Q(name__contains=query) |
    #                      Q(room_status__name__contains=query) |
    #                      Q(room_type__name__contains=query)).distinct()

    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'User List', 'lst': data_rows}
    return render(request, 'user/list.html', context=context)


def person_create(request):
    try:
        if request.method == 'POST':
            form = PersonForm(request.POST or None)
            if form.is_valid():
                instance = form.save()
                # instance.password = instance.set instance.password
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'user/create.html', context={'title': 'New User', 'form': PersonForm()})


def person_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Person, id=id)
        form = PersonForm(request.POST or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:persons')
        context = {
            'title': 'Person Edit',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'user/edit.html', context=context)


def person_delete(request, id=None):
    try:
        instance = get_object_or_404(Person, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:persons')


# Report:
# def report_paymentbydate(request):
#     query = request.GET.get('q')
#     if query == None:
#         query = datetime.datetime(2019, 5, 10)
#     else:
#         query = datetime.datetime.strptime(query, '%Y-%m-%d')
#     lst = InvoiceDetail.objects.filter(date_order__gte=query.date(), date_order__lte=query.date() + datetime.timedelta(days=1)) #start__gte=d.date(), start__lt=d.date()+timedelta(days=1)
#     sum_total = lst.aggregate(total=Sum(F('quantity') * F('price_confirm')))
#     context = {'title': 'User List', 'lst': lst, 'sum_total':sum_total }
#     return render(request, 'report/paymentbydate.html', context=context)


# Report:
def report_paymentbymoth(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 10)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    booking_payments = BookingPayment.objects.all().filter(date_pay__month=query.month)
    booking_ids = booking_payments.values_list('booking_id', flat=True).distinct()
    bookings = Guest.objects.all().filter(booking_id__in=booking_ids)
    booking2s = []
    cash_total = 0
    credit_total = 0
    bank_total = 0
    index = 1
    for booking in bookings:
        booking.pays = []
        bkp = booking_payments.filter(booking_id=booking.id)
        bkp_cash = bkp.filter(payment_type=1).count()
        bkp_cedit = bkp.filter(payment_type=2).count()
        bkp_bank = bkp.filter(payment_type=3).count()
        booking.orderNo = index
        for pay in bkp:
            a = list()
            a.append(pay.id)
            a.append(pay.credit)
            a.append(str(pay.date_pay))
            a.append(pay.desciption)
            a.append(pay.deposit)
            a.append(pay.booking_id)
            a.append(pay.payment_type_id)
            if pay.payment_type_id == 1:
                cash_total += pay.credit
            elif pay.payment_type_id == 2:
                credit_total += pay.credit
            else:
                bank_total += pay.credit
            booking2s.append(a)
            booking.pays.append(a)
        booking.max_count_record = max([bkp_cash, bkp_cedit, bkp_bank])
        index += 1

    context = {'title': 'Room Rate Report', 'bookings': bookings, 'cash_total': cash_total,
               'credit_total': credit_total, 'bank_total': bank_total, 'booking2s': booking2s}
    return render(request, 'report/roomratereport.html', context=context)


# def report_paymentbydate(request):
#     query = request.GET.get('q')
#     if query == None:
#         query = datetime.datetime(2019, 5, 11)
#     else:
#         query = datetime.datetime.strptime(query, '%Y-%m-%d')
#
#     booking_payments = BookingPayment.objects.filter(date_pay__gte=query.date(),
#                                                      date_pay__lte=query.date() + datetime.timedelta(days=1))
#     bookings = Booking.objects.filter(bookingpayment__date_pay__gte=query.date(),
#                                       bookingpayment__date_pay__lte=query.date() + datetime.timedelta(days=1))
#     bk_ids = bookings.values_list('id', flat=True)
#     guests = Guest.objects.filter(pk__in=bk_ids)
#     context = {'title': 'User List', 'payments': booking_payments, 'bookings': bookings, 'guests': guests}
#     return render(request, 'report/paymentbydate.html', context=context)
#

def report_houseskeeping(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Booking.objects.filter(arrive_date__lte=query).filter(
        depart_date__gte=query).filter(~Q(booking_status__in=[3, 4, 5]))

    rooms = Room.objects.all()

    for item in rooms:
        bk = None
        try:
            bk = bookings.get(room_id=item.id)
            if bk.depart_date == query.date():
                item.room_status.abc = 'Check-out'
            elif bk.arrive_date == query.date():
                item.room_status.abc = 'Check-in'
            else:
                item.room_status.abc = 'In-House'
        except:
            continue

    context = {'title': 'HouseSkeeping Report', 'bookings': bookings, 'rooms': rooms}
    return render(request, 'report/houseskeeping.html', context=context)


def report_cancel(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=4).filter(booking__arrive_date__gte=query.date(),
                                                                               booking__arrive_date__lte=query.date() + datetime.timedelta(
                                                                                   days=1))
    context = {'title': 'Cancelation Report', 'bookings': bookings}
    return render(request, 'report/cancel.html', context=context)


def report_noshow(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=5).filter(booking__arrive_date__gte=query.date(),
                                                                               booking__arrive_date__lte=query.date() + datetime.timedelta(
                                                                                   days=1))
    context = {'title': 'No-Show Report', 'bookings': bookings}
    return render(request, 'report/noshow.html', context=context)


def report_breakfast(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')
    bookings = Guest.objects.all().filter(booking__arrive_date__lte=query) \
        .filter(booking__depart_date__gte=query). \
        filter(~Q(booking__booking_status__in=[1, 3, 4, 5])).filter(booking__is_breakfast=True)

    adult_total = 0
    child_total = 0

    for user in bookings:
        adult_total += user.booking.adult
        child_total += user.booking.child

    context = {'title': 'Breakfast List', 'bookings': bookings, 'adult_total': adult_total, 'child_total': child_total,
               'total_person': adult_total + child_total}
    return render(request, 'report/breakfast.html', context=context)


def report_checkin(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=1) \
        .filter(booking__depart_date__gte=query)
    context = {'title': 'Pedding Check-in Report', 'bookings': bookings}
    return render(request, 'report/checkin.html', context=context)


def report_checkout(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=3) \
        .filter(booking__depart_date=query)

    context = {'title': 'Pedding Check-out Report', 'bookings': bookings}
    return render(request, 'report/checkout.html', context=context)


def report_inhouse(request):
    bookings = Guest.objects.all().filter(booking__booking_status_id=2)
    context = {'title': 'In-House Report', 'bookings': bookings}
    return render(request, 'report/inhouse.html', context=context)


def report_paymentbydate(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 12)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')
    booking_payments = BookingPayment.objects.all().filter(date_pay__gte=query.date(),
                                                           date_pay__lte=query.date() + datetime.timedelta(days=1))
    booking_ids = booking_payments.values_list('booking_id', flat=True).distinct()
    bookings = Guest.objects.all().filter(booking_id__in=booking_ids)
    booking2s = []
    cash_total = 0
    credit_total = 0
    bank_total = 0
    index = 1
    for booking in bookings:
        booking.pays = []
        bkp = booking_payments.filter(booking_id=booking.id)
        bkp_cash = bkp.filter(payment_type=1).count()
        bkp_cedit = bkp.filter(payment_type=2).count()
        bkp_bank = bkp.filter(payment_type=3).count()
        booking.orderNo = index
        for pay in bkp:
            a = list()
            a.append(pay.id)
            a.append(pay.credit)
            a.append(str(pay.date_pay))
            a.append(pay.desciption)
            a.append(pay.deposit)
            a.append(pay.booking_id)
            a.append(pay.payment_type_id)
            if pay.payment_type_id == 1:
                cash_total += pay.credit
            elif pay.payment_type_id == 2:
                credit_total += pay.credit
            else:
                bank_total += pay.credit
            booking2s.append(a)
            booking.pays.append(a)
        booking.max_count_record = max([bkp_cash, bkp_cedit, bkp_bank])
        index += 1

    context = {'title': 'Room Rate Report', 'bookings': bookings, 'cash_total': cash_total,
               'credit_total': credit_total, 'bank_total': bank_total, 'booking2s': booking2s}
    return render(request, 'report/roomratereport.html', context=context)


def report_roompayment(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 12)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = InvoiceDetail.objects.all().filter(product_id=1).filter(date_order__gte=query.date(),
                                                           date_order__lte=query.date() + datetime.timedelta(days=1))
    sum_total = bookings.aggregate(tota3l=Sum(F('quantity') * F('price_confirm')))
    context = {'title': 'Room Payment Report', 'bookings': bookings, 'sum_total':sum_total}
    return render(request, 'report/roompayment.html', context=context)




def report_extrapayment(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 12)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = InvoiceDetail.objects.all().filter(~Q(product_id=1)).filter(date_order__gte=query.date(),
                                                           date_order__lte=query.date() + datetime.timedelta(days=1))
    sum_total = bookings.aggregate(tota3l=Sum(F('quantity') * F('price_confirm')))
    context = {'title': 'Extra Payment Report', 'bookings': bookings, 'sum_total':sum_total}
    return render(request, 'report/extrapayment.html', context=context)