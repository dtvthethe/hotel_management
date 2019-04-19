import axios from 'axios'
import { format } from 'date-fns'
import { URL_API } from '../config'

const state = {
    rooms: [],
    guests_bookings: [],
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
    }
}

const mutations = {
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
                state.guests_bookings = res.data;
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
        let booking_data = {
            booking_status: 2
        };
        axios.put(URL_API + 'api/booking_checkin/' + data.booking_id,
            booking_data
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
        axios.put(URL_API + 'api/booking_updatefoliotransfer/' + data.booking.id,
            data.booking.data
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    removeCalendarBooking: function (state, id) {
        let bk = state.guests_bookings.find(item => item.booking.id == id);
        if (bk) {
            let index = state.guests_bookings.indexOf(bk);
            state.guests_bookings.splice(index, 1);
        }
    },

}

const actions = {
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
    updateBookingFolioTransfer: function ({ commit, rootState }, booking_data) {
        commit('updateBookingFolioTransfer', {
            'booking': booking_data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateBookingCheckIn: function ({ commit, rootState }, booking_data) {
        commit('updateBookingCheckIn', {
            'booking_id': booking_data,
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
