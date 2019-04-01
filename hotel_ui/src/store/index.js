import Vue from 'vue'
import Vuex from 'vuex'
import ui_module from './modules/ui_module'
import booking_module from './modules/booking_module'
import frontdesk_module from './modules/frontdesk_module'
import reveration_module from './modules/reveration_module'
import product_module from './modules/product_module'
import producttypes_module from './modules/producttypes_module'


Vue.use(Vuex);
export default new Vuex.Store({
    modules: {
        ui_module,
        booking_module,
        frontdesk_module,
        reveration_module,
        product_module,
        producttypes_module
    }
});