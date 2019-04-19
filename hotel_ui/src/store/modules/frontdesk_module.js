import axios from 'axios'
import { URL_API } from '../config'

const state = {
    room_list: [],
    bookings: []
}

const getters = {
    getRoomWithTypes: function (state) {
        return state.room_list;
    },
    getBookings: function (state) {
        return state.bookings;
    }
}

const mutations = {
    fetchRoomWithTypes: function (state, header_config) {
        axios.get(URL_API + 'api/room_roomtypes', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.room_list = res.data;
            }
            else {
                state.room_list = [];
            }
        });
    },
    fetchBookings: function (state, data) {
        axios.get(URL_API + 'api/guest_booking?session_date=' + data.session_date, {
            headers: {
                ...data.header
            }
        }).then(res => {
            if (res.status == 200) {
                state.bookings = res.data;
            }
            else {
                state.bookings = [];
            }
        });
    },
    removeBookings: function (state, id) {
        let bk = state.bookings.find(item => item.id == id);
        if (bk) {
            let index = state.bookings.indexOf(bk);
            state.bookings.splice(index, 1);
        }
    }
}

const actions = {
    fetchRoomWithTypes: function ({ commit, rootState }) {
        commit('fetchRoomWithTypes', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    fetchBookings: function ({ commit, rootState }, session_date) {
        commit('fetchBookings', {
            session_date,
            header: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    removeBookings({ commit }, id) {
        commit('removeBookings', id);
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}