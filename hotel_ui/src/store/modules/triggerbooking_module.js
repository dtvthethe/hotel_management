import axios from 'axios'
import { format } from 'date-fns'
import { URL_API } from '../config'
import Booking from '../../models/booking'
import Guest from '../../models/guest'

const state = {
    booking_detail: {},
    booking_guest_detail: {},
    clients: [],
    rooms: [],
    room_types: []
}
const getters = {
    getBookingDetail: function (state) {
        return state.booking_detail;
    },
    getBookingGuestDetail: function (state) {
        return state.booking_guest_detail;
    },
    getClients: function (state) {
        return state.clients;
    },
    getRoomTypes: function (state) {
        return state.room_types;
    }
}
const mutations = {
    setBookingDetail: function (state) {
        state.booking_detail = 'hihihi';
        state.booking_guest_detail = 'hahaha';
    },
    setBookingDetailDeafault: function (state) {
        state.booking_detail = new Booking();
        state.booking_guest_detail = new Guest();
    },
    fetchClientList: function (state) {
        axios.get(URL_API + 'api/clients').then(res => {
            if (res.status == 200) {
                state.clients = res.data;
            }
            else {
                state.clients = [];
            }
        });
    },
    fetchRoomTypeList: function (state) {
        axios.get(URL_API + 'api/roomtypes').then(res => {
            if (res.status == 200) {
                state.room_types = res.data;
            }
            else {
                state.room_types = [];
            }
        });
    },
    postReveration: function (state) {
        let booking = {
            ...state.booking_detail,
            arrive_date: format(state.booking_detail.arrive_date, 'YYYY-MM-DD'),
            depart_date: format(state.booking_detail.depart_date, 'YYYY-MM-DD'),
            guest: state.booking_guest_detail
        };
        axios.post(URL_API + 'api/new_reveration',
            booking
        ).then(res => {
            console.log(res);
        }).catch(ex => {
            console.log(ex);
        })
    },

    setBookingCode(state, value) {
        state.booking_detail.booking_code = value;
    },
    setBookingAdult(state, value) {
        state.booking_detail.adult = value;
    },
    setBookingChild(state, value) {
        state.booking_detail.child = value;
    },
    setBookingNote(state, value) {
        state.booking_detail.note = value;
    },
    setBookingArriveDate(state, value) {
        state.booking_detail.arrive_date = value;
    },
    setBookingDepartDate(state, value) {
        state.booking_detail.depart_date = value;
    },
    setBookingIsBreakfast(state, value) {
        state.booking_detail.is_breakfast = value;
    },
    setBookingPriceBooking(state, value) {
        state.booking_detail.price_booking = value;
    },
    setBookingClient(state, value) {
        state.booking_detail.client = value;
    },
    setBookingRoom(state, value) {
        state.booking_detail.room = value;
    },

    setFullname(state, value) {
        state.booking_guest_detail.fullname = value;
    },

}
const actions = {
    fetchBookingDetail: function ({ commit }, data) {
        commit('setBookingDetail', data);
    },
    setBookingDetailDeafault: function ({ commit }) {
        commit('setBookingDetailDeafault');
    },
    fetchClientList: function ({ commit }) {
        commit('fetchClientList');
    },
    fetchRoomTypeList: function ({ commit }) {
        commit('fetchRoomTypeList');
    },
    postReveration: function ({ commit }) {
        commit('postReveration');
    },

    setBookingCode({ commit }, value) {
        commit('setBookingCode', value);
    },
    setBookingAdult({ commit }, value) {
        commit('setBookingAdult', value);
    },
    setBookingChild({ commit }, value) {
        commit('setBookingChild', value);
    },
    setBookingNote({ commit }, value) {
        commit('setBookingNote', value);
    },
    setBookingArriveDate({ commit }, value) {
        commit('setBookingArriveDate', value);
    },
    setBookingDepartDate({ commit }, value) {
        commit('setBookingDepartDate', value);
    },
    setBookingIsBreakfast({ commit }, value) {
        commit('setBookingIsBreakfast', value);
    },
    setBookingPriceBooking({ commit }, value) {
        commit('setBookingPriceBooking', value);
    },
    setBookingClient({ commit }, value) {
        commit('setBookingClient', value);
    },
    setBookingRoom({ commit }, value) {
        commit('setBookingRoom', value);
    },
    setFullname({ commit }, value) {
        commit('setFullname', value);
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}