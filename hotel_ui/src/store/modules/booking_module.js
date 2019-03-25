import axios from 'axios'
import {URL_API} from '../config'

const state = {
    rooms: [],
    guests_bookings: [],
}

const getters = {
    getRooms: function (state) {
        return state.rooms;
    },
    getGuestBookings: function (state) {
        return state.guests_bookings;
    }
}

const mutations = {
    fetchRooms: function (state) {
        axios.get(URL_API+'api/rooms').then(res => {
            if (res.status == 200) {
                state.rooms = res.data;
            }
            else{
                state.rooms = [];
            }
        });
    },
    fetchGuestBookings: function(state, bk_date){
        axios.get(URL_API+'api/guest_bookings?arrive_date='+bk_date.arrive_date+'&depart_date='+bk_date.depart_date).then(res => {
            if (res.status == 200) {
                state.guests_bookings = res.data;
            }
            else{
                state.rooms = [];
            }
        });
    }
}

const actions = {
    fetchRooms: function ({ commit }) {
        commit('fetchRooms');
    },
    fetchGuestBookings: function({commit}, bk_date){
        commit('fetchGuestBookings', bk_date);
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}