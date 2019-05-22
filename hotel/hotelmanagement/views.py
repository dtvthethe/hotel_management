import datetime

from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Q, F, Sum
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from hotelmanagement.forms import ProductTypeForm, RoomTypeForm, ClientForm, ConfigForm, PaymentTypeForm, ProductForm, \
    RoomForm, PersonForm, PersonEditForm, PersonChangePasswordForm, LoginForm
from .models import ProductType, RoomType, Client, Config, PaymentType, Product, Room, Person, Invoice, InvoiceDetail, \
    BookingPayment, Booking, Guest


# ProductType
@login_required(login_url='/login')
def producttype_list(request):
    lst = ProductType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Product Type List', 'lst': data_rows}
    return render(request, 'producttype/list.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def producttype_delete(request, id=None):
    try:
        instance = get_object_or_404(ProductType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:producttypes')


# RoomType
@login_required(login_url='/login')
def roomtype_list(request):
    lst = RoomType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Room Type List', 'lst': data_rows}
    return render(request, 'roomtype/list.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def roomtype_delete(request, id=None):
    try:
        instance = get_object_or_404(RoomType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:roomtypes')


# Client
@login_required(login_url='/login')
def cient_list(request):
    lst = Client.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Client List', 'lst': data_rows}
    return render(request, 'client/list.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def client_delete(request, id=None):
    try:
        instance = get_object_or_404(Client, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:clients')


# Config
@login_required(login_url='/login')
def config_list(request):
    lst = Config.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Config List', 'lst': data_rows}
    return render(request, 'config/list.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def config_delete(request, id=None):
    try:
        instance = get_object_or_404(Config, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:configs')


# Payment Type
@login_required(login_url='/login')
def paymenttype_list(request):
    lst = PaymentType.objects.all()
    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'Payment Type List', 'lst': data_rows}
    return render(request, 'paymenttype/list.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def paymenttype_delete(request, id=None):
    try:
        instance = get_object_or_404(PaymentType, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:paymenttypes')


# Product
@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def product_delete(request, id=None):
    try:
        instance = get_object_or_404(Product, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:products')


# Room
@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def room_delete(request, id=None):
    try:
        instance = get_object_or_404(Room, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:rooms')


# Person
@login_required(login_url='/login')
def person_list(request):
    lst = Person.objects.all()
    query = request.GET.get('q')
    if query:
        lst = lst.filter(Q(username__contains=query) | Q(email__contains=query) | Q(first_name__contains=query) |
                         Q(last_name__contains=query)).distinct()

    paginator = Paginator(lst, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)
    context = {'title': 'User List', 'lst': data_rows}
    return render(request, 'user/list.html', context=context)


@login_required(login_url='/login')
def person_create(request):
    try:
        if request.method == 'POST':
            form = PersonForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                instance = form.save(commit=False)
                instance.set_password(instance.password)
                instance.save()
                messages.success(request, 'Create successfully!')
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'user/create.html', context={'title': 'New User', 'form': PersonForm()})


@login_required(login_url='/login')
def person_edit(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Person, id=id)
        form = PersonEditForm(request.POST or None, request.FILES or None, instance=instance)
        if form.is_valid():
            form.save()
            messages.success(request, 'Update successfully!')
            return redirect('hotelmanagement_namspace:persons')
        context = {
            'title': 'User Update',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'user/edit.html', context=context)


@login_required(login_url='/login')
def person_changepassword(request, id=None):
    context = None
    try:
        instance = get_object_or_404(Person, id=id)
        form = PersonChangePasswordForm(request.POST or None, instance=instance)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.set_password(obj.password)
            obj.save()
            messages.success(request, 'Change password successfully!')
            return redirect('hotelmanagement_namspace:persons')
        context = {
            'title': 'Change password',
            'form': form
        }
    except BaseException as be:
        messages.error(request, be)
    return render(request, 'user/edit.html', context=context)


@login_required(login_url='/login')
def person_delete(request, id=None):
    try:
        instance = get_object_or_404(Person, id=id)
        instance.delete()
        messages.success(request, 'Delete successfully!')
    except BaseException as be:
        messages.error(request, be)
    return redirect('hotelmanagement_namspace:persons')


# Report:
@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def report_checkin(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=1) \
        .filter(booking__arrive_date=query)
    context = {'title': 'Pending Check-in Report', 'bookings': bookings}
    return render(request, 'report/checkin.html', context=context)


@login_required(login_url='/login')
def report_checkout(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 3, 9)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = Guest.objects.all().filter(booking__booking_status_id=3) \
        .filter(booking__depart_date=query)

    context = {'title': 'Pending Check-out Report', 'bookings': bookings}
    return render(request, 'report/checkout.html', context=context)


@login_required(login_url='/login')
def report_inhouse(request):
    bookings = Guest.objects.all().filter(booking__booking_status_id=2)
    context = {'title': 'In-House Report', 'bookings': bookings}
    return render(request, 'report/inhouse.html', context=context)


@login_required(login_url='/login')
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


@login_required(login_url='/login')
def report_roompayment(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 12)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = InvoiceDetail.objects.all().filter(product_id=1).filter(date_order__gte=query.date(),
                                                                       date_order__lte=query.date() + datetime.timedelta(
                                                                           days=1))
    sum_total = bookings.aggregate(tota3l=Sum(F('quantity') * F('price_confirm')))
    context = {'title': 'Room Payment Report', 'bookings': bookings, 'sum_total': sum_total}
    return render(request, 'report/roompayment.html', context=context)


@login_required(login_url='/login')
def report_extrapayment(request):
    query = request.GET.get('q')
    if query == None:
        query = datetime.datetime(2019, 5, 12)
    else:
        query = datetime.datetime.strptime(query, '%Y-%m-%d')

    bookings = InvoiceDetail.objects.all().filter(~Q(product_id=1)).filter(date_order__gte=query.date(),
                                                                           date_order__lte=query.date() + datetime.timedelta(
                                                                               days=1))
    sum_total = bookings.aggregate(tota3l=Sum(F('quantity') * F('price_confirm')))
    context = {'title': 'Extra Payment Report', 'bookings': bookings, 'sum_total': sum_total}
    return render(request, 'report/extrapayment.html', context=context)


def login_auth(request):
    context = None
    try:
        if request.user.is_authenticated is True:
            return redirect('hotelmanagement_namspace:persons')

        form = LoginForm(request.POST or None)
        user = None
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
        context = {
            'form': form
        }
        if user is not None:
            if user.is_active and user.is_superuser:
                per = Person.objects.get(user=user)
                login(request, per)
                return redirect('hotelmanagement_namspace:persons')
            else:
                messages.error(request, "You do not have any permission to access this page!")
        else:
            messages.error(request, "Username or password doesn't correct")
        return render(request, 'auth/login.html', context=context)

    except BaseException as be:
        messages.error(request, be)
        return render(request, 'auth/login.html', context=context)


@login_required(login_url='/login')
def logout_auth(request):
    logout(request)
    return redirect('hotelmanagement_namspace:login')


@login_required(login_url='/login')
def notify_nummer(request):
    query = datetime.datetime(2019, 3, 9)
    pennding_checkin = Guest.objects.all().filter(booking__booking_status_id=1) \
        .filter(booking__arrive_date=query).count()

    pennding_checkout = Guest.objects.all().filter(booking__booking_status_id=3) \
        .filter(booking__depart_date=query).count()
    context = {
        'pennding_checkin': pennding_checkin,
        'pennding_checkout': pennding_checkout
    }
    return render(request, 'notify/nummer.html', context=context)

@login_required(login_url='/login')
def quick_search(request):
    query = request.GET.get('q')
    lst = Person.objects.filter(Q(username__contains=query) | Q(email__contains=query) | Q(first_name__contains=query) |
                     Q(last_name__contains=query)).distinct()
    context = {
        'persons': lst,
    }
    return render(request, 'user/quick_search.html', context=context)

@login_required(login_url='/login')
def index(request):
    query = datetime.datetime(2019, 3, 9)
    pennding_checkin = Guest.objects.all().filter(booking__booking_status_id=1) \
        .filter(booking__arrive_date=query).count()

    pennding_checkout = Guest.objects.all().filter(booking__booking_status_id=3) \
        .filter(booking__depart_date=query).count()

    in_house = Guest.objects.all().filter(booking__booking_status_id=2).count()


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

    paginator = Paginator(rooms, 10)
    page = request.GET.get('page')
    data_rows = paginator.get_page(page)

    context = {
        'title':'Dashboard',
        'pennding_checkin': pennding_checkin,
        'pennding_checkout': pennding_checkout,
        'in_house':in_house,
        'rooms':data_rows
    }

    return render(request, 'dashboard/index.html', context=context)
