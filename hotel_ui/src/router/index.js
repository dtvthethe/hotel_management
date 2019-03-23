import Vue from 'vue'
import VueRouter from 'vue-router'

import FrontDesk from '../components/FrontDesk'
import CalendarBooking from '../components/CalendarBooking'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        { path: '/', component: FrontDesk },
        { path: '/calendar', component: CalendarBooking },
    ]
});