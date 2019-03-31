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
    fetchRooms: function (state) {
        axios.get(URL_API + 'api/rooms').then(res => {
            if (res.status == 200) {
                state.rooms = res.data;
            }
            else {
                state.rooms = [];
            }
        });
    },
    fetchGuestBookings: function (state, bk_date) {
        axios.get(URL_API + 'api/guest_bookings?arrive_date=' + bk_date.arrive_date + '&depart_date=' + bk_date.depart_date).then(res => {
            if (res.status == 200) {
                state.guests_bookings = res.data;
            }
            else {
                state.rooms = [];
            }
        });
    },
    updateBooking: function (state, booking) {
        let booking_data = {
            ...booking,
            arrive_date: format(booking.arrive_date, 'YYYY-MM-DD'),
            depart_date: format(booking.depart_date, 'YYYY-MM-DD'),
        };
        axios.put(URL_API + 'api/booking_update/' + booking_data.id,
            booking_data
        ).then().catch()
    },
    removeCalendarBooking:function(state, id){
        let bk = state.guests_bookings.find(item => item.booking.id == id);
        if (bk){
            let index = state.guests_bookings.indexOf(bk);
            state.guests_bookings.splice(index, 1);
        }
    },

}

const actions = {
    fetchRooms: function ({ commit }) {
        commit('fetchRooms');
    },
    fetchGuestBookings: function ({ commit }, bk_date) {
        commit('fetchGuestBookings', bk_date);
    },
    updateBooking({ commit }, booking) {
        commit('updateBooking', booking);
    },
    removeCalendarBooking({commit}, id){
        commit('removeCalendarBooking', id);
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}