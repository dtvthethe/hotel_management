import axios from 'axios'
import { format, parse } from 'date-fns'
import { URL_API } from '../config'
import Booking from '../../models/booking'
import Guest from '../../models/guest'

const state = {
    frm_type: {
        type: 'fo', //  fo, ca
        method: 'new',// new, edit
        data_value: null,
        date_start: null,
        date_stop: null,
    },
    booking_detail: {},
    booking_guest_detail: {},
    clients: [],
    rooms: [],
    room_types: [],
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
    },
    getFrmType(state) {
        return state.frm_type;
    },
}
const mutations = {
    setBookingDetailDeafault: function (state) {
        state.booking_detail = new Booking();
        state.booking_guest_detail = new Guest();
    },
    fetchClientList: function (state, header_config) {
        axios.get(URL_API + 'api/clients', {
            headers: {
                ...header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.clients = res.data;
            }
            else {
                state.clients = [];
            }
        });
    },
    fetchRoomTypeList: function (state, header_config) {
        axios.get(URL_API + 'api/roomtypes', {
            headers: {
                ...header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.room_types = res.data;
            }
            else {
                state.room_types = [];
            }
        });
    },
    fetchGuestBookingDetail: function (state, data) {
        state.booking_detail = new Booking();
        state.booking_guest_detail = new Guest();
        axios.get(URL_API + 'api/guestbookingdetail/' + data.data.id, {
            headers: {
                ...data.header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.booking_guest_detail.fullname = res.data.fullname;
                state.booking_guest_detail.id = res.data.id;
                state.booking_guest_detail.booking = res.data.booking.id;
                state.booking_detail = res.data.booking;
                state.booking_detail.arrive_date = parse(res.data.booking.arrive_date);
                state.booking_detail.depart_date = parse(res.data.booking.depart_date);
            }
        });
    },
    postReveration: function (state, header_config) {
        let booking = {
            ...state.booking_detail,
            arrive_date: format(state.booking_detail.arrive_date, 'YYYY-MM-DD'),
            depart_date: format(state.booking_detail.depart_date, 'YYYY-MM-DD'),
            guest: state.booking_guest_detail,
            booking_status: 1,
        };
        axios.post(URL_API + 'api/new_reveration',
            booking, {
                headers: {
                    ...header_config
                }
            }
        ).then().catch();
    },
    updateReveration: function (state, header_config) {
        let booking = {
            ...state.booking_detail,
            arrive_date: format(state.booking_detail.arrive_date, 'YYYY-MM-DD'),
            depart_date: format(state.booking_detail.depart_date, 'YYYY-MM-DD'),
            guest: state.booking_guest_detail,
        };
        axios.put(URL_API + 'api/reveration_update/' + state.booking_detail.id,
            booking, {
                headers: {
                    ...header_config
                }
            }
        ).then().catch()
    },
    deleteReveration: function (state, data) {
        axios.delete(URL_API + 'api/reveration_delete/' + data.data.id, {
            headers: {
                ...data.header_config
            }
        }).then().catch()
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
    setFrmType(state, frm_type) {
        state.frm_type = frm_type;
    },

}
const actions = {
    fetchGuestBookingDetail: function ({ commit, rootState }, data) {
        commit('fetchGuestBookingDetail', {
            data: data.data_booking, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
        commit('fetchInvoiceDetails', {
            guest_booking: data.guest_booking,
            header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    setBookingDetailDeafault: function ({ commit }) {
        commit('setBookingDetailDeafault');
    },
    fetchClientList: function ({ commit, rootState }) {
        commit('fetchClientList', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    fetchRoomTypeList: function ({ commit, rootState }) {
        commit('fetchRoomTypeList', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postReveration: function ({ commit, rootState }) {
        commit('postReveration', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    updateReveration: function ({ commit, rootState }) {
        commit('updateReveration', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    deleteReveration: function ({ commit, rootState }, data) {
        commit('deleteReveration', {
            data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
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
    setFrmType({ commit }, frm_type) {
        commit('setFrmType', frm_type);
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}