import axios from 'axios'
import { URL_API } from '../config'

const state = {
    room_list: [],
    bookings:[]
}

const getters = {
    getRoomWithTypes: function (state) {
        return state.room_list;
    },
    getBookings:function(state){
        return state.bookings;
    }
}

const mutations = {
    fetchRoomWithTypes: function (state) {
        axios.get(URL_API+'api/room_roomtypes').then(res => {
            if (res.status == 200) {
                state.room_list = res.data;
            }
            else{
                state.room_list = [];
            }
        });
    },
    fetchBookings:function(state, session_date){
        axios.get(URL_API+'api/guest_booking?session_date='+session_date).then(res => {
            if (res.status == 200) {
                state.bookings = res.data;
            }
            else{
                state.bookings = [];
            }
        });
    },
    removeBookings:function(state, id){
        let bk = state.bookings.find(item => item.id == id);
        if (bk){
            let index = state.bookings.indexOf(bk);
            state.bookings.splice(index, 1);
        }
    }
}

const actions = {
    fetchRoomWithTypes: function ({commit}) {
        commit('fetchRoomWithTypes');
    },
    fetchBookings: function({commit}, session_date){
        commit('fetchBookings', session_date);
    },
    removeBookings({commit}, id){
        commit('removeBookings', id);
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}