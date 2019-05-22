from django.urls import path
from . import views

app_name = 'hotelmanagement_namspace'

urlpatterns = [
    path('producttypes', views.producttype_list, name='producttypes'),
    path('producttypes/create', views.producttype_create, name='producttypes_create'),
    path('producttypes/edit/<int:id>', views.producttype_edit, name='producttypes_edit'),
    path('producttypes/delete/<int:id>', views.producttype_delete, name='producttypes_delete'),

    path('roomtypes', views.roomtype_list, name='roomtypes'),
    path('roomtypes/create', views.roomtype_create, name='roomtypes_create'),
    path('roomtypes/edit/<int:id>', views.roomtype_edit, name='roomtypes_edit'),
    path('roomtypes/delete/<int:id>', views.roomtype_delete, name='roomtypes_delete'),

    path('clients', views.cient_list, name='clients'),
    path('clients/create', views.client_create, name='client_create'),
    path('clients/edit/<int:id>', views.client_edit, name='client_edit'),
    path('clients/delete/<int:id>', views.client_delete, name='client_delete'),

    path('configs', views.config_list, name='configs'),
    path('configs/create', views.config_create, name='config_create'),
    path('configs/edit/<int:id>', views.config_edit, name='config_edit'),
    path('configs/delete/<int:id>', views.config_delete, name='config_delete'),

    path('paymenttypes', views.paymenttype_list, name='paymenttypes'),
    path('paymenttypes/create', views.paymenttype_create, name='paymenttype_create'),
    path('paymenttypes/edit/<int:id>', views.paymenttype_edit, name='paymenttype_edit'),
    path('paymenttypes/delete/<int:id>', views.paymenttype_delete, name='paymenttype_delete'),

    path('products', views.product_list, name='products'),
    path('products/create', views.product_create, name='product_create'),
    path('products/edit/<int:id>', views.product_edit, name='product_edit'),
    path('products/delete/<int:id>', views.product_delete, name='product_delete'),

    path('rooms', views.room_list, name='rooms'),
    path('rooms/create', views.room_create, name='room_create'),
    path('rooms/edit/<int:id>', views.room_edit, name='room_edit'),
    path('rooms/delete/<int:id>', views.room_delete, name='room_delete'),

    path('persons', views.person_list, name='persons'),
    path('persons/create', views.person_create, name='person_create'),
    path('persons/edit/<int:id>', views.person_edit, name='person_edit'),
    path('persons/delete/<int:id>', views.person_delete, name='person_delete'),
    path('persons/change_password/<int:id>', views.person_changepassword, name='change_password'),

    path('report/houseskeeping', views.report_houseskeeping, name='report_houseskeeping'),
    path('report/cancel', views.report_cancel, name='report_cancel'),
    path('report/noshow', views.report_noshow, name='report_noshow'),
    path('report/breakfast', views.report_breakfast, name='report_breakfast'),
    path('report/pending_checkin', views.report_checkin, name='report_pending_checkin'),
    path('report/pending_checkout', views.report_checkout, name='report_pending_checkout'),
    path('report/pending_inhouse', views.report_inhouse, name='report_inhouse'),
    path('report/pamentbymonth', views.report_paymentbymoth, name='report_pamentbymonth'),
    path('report/paymentbydate', views.report_paymentbydate, name='report_paymentbydate'),
    path('report/roompayment', views.report_roompayment, name='report_roompayment'),
    path('report/extrapayment', views.report_extrapayment, name='report_extrapayment'),

    path('login', views.login_auth, name='login'),
    path('logout', views.logout_auth, name='logout'),
    path('notify_nummer', views.notify_nummer, name='notify_nummer'),
    path('quick_search', views.quick_search, name='quick_search'),
    path('', views.index, name='index'),

]
