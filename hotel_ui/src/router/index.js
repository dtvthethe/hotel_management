import Vue from 'vue'
import VueRouter from 'vue-router'

import FrontDesk from '../components/FrontDesk'
import CalendarBooking from '../components/CalendarBooking'
import User from '../components/User'
import RoomType from '../components/RoomType'
import ProductType from '../components/ProductType'
import Product from '../components/Product'
import Room from '../components/Room'
import RoomStatus from '../components/RoomStatus'
import NightAudit from '../components/NightAudit'
import GuestLeger from '../components/GuestLeger'

Vue.use(VueRouter)

export default new VueRouter({
    mode: 'history',
    base: __dirname,
    routes: [
        { path: '/', component: FrontDesk },
        { path: '/calendar', component: CalendarBooking },
        { path: '/user', component: User },
        { path: '/roomtype', component: RoomType },
        { path: '/producttype', component: ProductType },
        { path: '/product', component: Product },
        { path: '/room', component: Room },
        { path: '/roomstatus', component: RoomStatus },
        { path: '/nightaudit', component: NightAudit },
        { path: '/guestleger', component: GuestLeger },
    ]
});