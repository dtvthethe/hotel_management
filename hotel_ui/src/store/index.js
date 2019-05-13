import Vue from 'vue'
import Vuex from 'vuex'
import ui_module from './modules/ui_module'
import booking_module from './modules/booking_module'
import frontdesk_module from './modules/frontdesk_module'
import reveration_module from './modules/reveration_module'
import product_module from './modules/product_module'
import producttypes_module from './modules/producttypes_module'
import bookingpayment_module from './modules/bookingpayment_module'
import paymenttype_module from './modules/paymenttype_module'
import config_module from './modules/config_module'
import user_module from './modules/user_module'
import userpermission_module from './modules/userpermission_module'
import roomtype_module from './modules/roomtype_module'
import producttype_module from './modules/producttype_module'
import room_module from './modules/room_module'
import roomstatus_module from './modules/roomstatus_module'
import invoice_module from './modules/invoice_module'



Vue.use(Vuex);
export default new Vuex.Store({
    modules: {
        ui_module,
        booking_module,
        frontdesk_module,
        reveration_module,
        product_module,
        producttypes_module,
        bookingpayment_module,
        paymenttype_module,
        config_module,
        user_module,
        userpermission_module,
        roomtype_module,
        producttype_module,
        room_module,
        roomstatus_module,
        invoice_module,
    }
});