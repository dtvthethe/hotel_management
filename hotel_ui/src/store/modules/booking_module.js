import axios from 'axios'
import { format } from 'date-fns'
import { URL_API } from '../config'

const state = {
    rooms: [],
    guests_bookings: [],
    error_transfer: null,
    nightaudits:[],
    guestlegers:[]
}

const getters = {
    getRooms: (state) => (id) => {
        if (id == -1) {
            return state.rooms;
        }
        else {
            return state.rooms.filter(item => item.room_type == id);
        }
    },
    getGuestBookings: function (state) {
        return state.guests_bookings;
    },
    getErrorTransfer: function (state) {
        return state.error_transfer;
    },
    getNightAudit(state){
        return state.nightaudits;
    },
    getGuestLeger(state){
        return state.guestlegers;
    }
}

const mutations = {
    fetchGuestLeger: function (state, data) {
        let query = '?client='+data.query.client;
        if(data.query.booking_id != null && data.query.booking_id.length > 0){
            query += '&booking_id='+data.query.booking_id;
        }
        if(data.query.fullname != null && data.query.fullname.length > 0){
            query += '&fullname='+data.query.fullname;
        }

        if(data.query.isFilterDate == true){
            if(data.query.arrive_date != null && data.query.arrive_date.length > 0){
                query += '&arrive_date='+data.query.arrive_date;
            }
            if(data.query.depart_date != null && data.query.depart_date.length > 0){
                query += '&depart_date='+data.query.depart_date;
            }
        }

        axios.get(URL_API + 'api/guestlegers'+query, {
            headers: {
                ...data.header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.guestlegers = res.data;
            }
            else {
                state.guestlegers = [];
            }
        });
    },
    removeGuestLeger: function (state, id) {
        let bk = state.guestlegers.find(item => item.id == id);
        if (bk) {
            let index = state.guestlegers.indexOf(bk);
            state.guestlegers.splice(index, 1);
        }
    },
    fetchRooms: function (state, header_config) {
        axios.get(URL_API + 'api/rooms', {
            headers: {
                ...header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.rooms = res.data;
            }
            else {
                state.rooms = [];
            }
        });
    },
    fetchGuestBookings: function (state, data) {
        axios.get(URL_API + 'api/guest_bookings?arrive_date=' + data.bk_date.arrive_date + '&depart_date=' + data.bk_date.depart_date, {
            headers: {
                ...data.header_config
            }
        }).then(res => {
            if (res.status == 200) {
                // state.guests_bookings = res.data;
                state.guests_bookings = res.data.filter(item => item.booking.booking_status.id <= 3);
            }
            else {
                state.rooms = [];
            }
        });
    },
    updateBooking: function (state, data) {
        let booking_data = {
            ...data.booking,
            arrive_date: format(data.booking.arrive_date, 'YYYY-MM-DD'),
            depart_date: format(data.booking.depart_date, 'YYYY-MM-DD'),
        };
        axios.put(URL_API + 'api/booking_update/' + booking_data.id,
            booking_data
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingCheckIn: function (state, data) {
        let invoice_data = {
            booking_status: 2,
            booking_id: parseInt(data.booking_id),
            guest_id: data.guest_id
        };
        axios.put(URL_API + 'api/checkin/' + data.booking_id,
            invoice_data
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingStatusCancel: function (state, data) {
        axios.put(URL_API + 'api/booking/update_status_noshow/' + data.booking.booking_id,
            {booking_status: 4}
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingStatusNoShow: function (state, data) {
        axios.put(URL_API + 'api/booking/update_status_noshow/' + data.booking.booking_id,
            {booking_status: 5}
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingStatusNoShowPostCharge: function (state, data) {
        axios.put(URL_API + 'api/booking/update_status_noshow_postcharge/' + data.booking.booking_id,
            {booking_status: 5, date_session: data.booking.date_session, price_confirm: data.booking.price_confirm}
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingCheckOut: function (state, data) {
        let booking_data = {
            booking_status: 3
        };
        axios.put(URL_API + 'api/booking_checkout/' + data.booking_id,
            booking_data
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateBookingFolioTransfer: function (state, data) {
        state.error_transfer = null;
        axios.put(URL_API + 'api/invoice/updatefoliotransfer/' + data.invoice.id,
            data.invoice.data
            , {
                headers: {
                    ...data.header_config
                }
            }).then(()=>{
                state.error_transfer = null;
            }).catch(() => {
                state.error_transfer = "This's ID unvalid to transfer";
            });

    },
    removeCalendarBooking: function (state, id) {
        let bk = state.guests_bookings.find(item => item.booking.id == id);
        if (bk) {
            let index = state.guests_bookings.indexOf(bk);
            state.guests_bookings.splice(index, 1);
        }
    },
    fetchNightAudit: function (state, data) {

        let url = 'api/nightaudits?depart_date='+format(data.data.date_f, 'YYYY-MM-DD')
        if(data.data.isArrive == true){
            url = 'api/nightaudits?arrive_date='+format(data.data.date_f, 'YYYY-MM-DD')
        }
        axios.get(URL_API + url, {
            headers: {
                ...data.header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.nightaudits = res.data;
            }
            else {
                state.nightaudits = [];
            }
        });
    },
}

const actions = {
    updateBookingStatusCancel({ commit, rootState }, booking) {
        commit('updateBookingStatusCancel', {
            booking, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateBookingStatusNoShow({ commit, rootState }, booking) {
        commit('updateBookingStatusNoShow', {
            booking, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateBookingStatusNoShowPostCharge({ commit, rootState }, booking) {
        commit('updateBookingStatusNoShowPostCharge', {
            booking, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    fetchGuestLeger: function ({ commit, rootState }, query) {
        commit('fetchGuestLeger', {
            query,
            header_config: {'Authorization': 'jwt ' + rootState.user_module.tokenAuth},
        });
    },
    fetchNightAudit: function ({ commit, rootState }, data) {
        commit('fetchNightAudit', {
            data,
            header_config: {'Authorization': 'jwt ' + rootState.user_module.tokenAuth},
        });
    },
    fetchRooms: function ({ commit, rootState }) {
        commit('fetchRooms', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    fetchGuestBookings: function ({ commit, rootState }, bk_date) {
        commit('fetchGuestBookings', {
            bk_date, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateBooking({ commit, rootState }, booking) {
        commit('updateBooking', {
            booking, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    removeCalendarBooking({ commit }, id) {
        commit('removeCalendarBooking', id);
    },
    removeGuestLeger({ commit }, id) {
        commit('removeGuestLeger', id);
    },
    updateBookingFolioTransfer: function ({ commit, rootState }, invoice_data) {
        commit('updateBookingFolioTransfer', {
            invoice: invoice_data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            },
        });
    },
    updateBookingCheckIn: function ({ commit, rootState }, booking_data) {
        commit('updateBookingCheckIn', {
            booking_id: booking_data.booking_id,
            guest_id: booking_data.guest_id,
            header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateBookingCheckOut: function ({ commit, rootState }, booking_data) {
        commit('updateBookingCheckOut', {
            'booking_id': booking_data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}
