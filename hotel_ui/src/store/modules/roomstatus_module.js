import axios from 'axios'
import { URL_API } from '../config'

const state = {
    roomstatus: []
}
const getters = {
    getRoomStatus(state) {
        return state.roomstatus;
    },
    
}
const mutations = {
    fetchRoomStatus(state, header_config) {
        axios.get(URL_API + 'api/roomstatus', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.roomstatus = res.data;
            }
            else {
                state.roomstatus = [];
            }
        });
    },
    
}

const actions = {
    fetchRoomStatus({ commit, rootState }) {
        commit('fetchRoomStatus', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    
}

export default {
    state,
    getters,
    actions,
    mutations
}