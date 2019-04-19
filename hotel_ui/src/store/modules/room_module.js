import axios from 'axios'
import { URL_API } from '../config'

const state = {
    rooms: []
}
const getters = {
    getRoomss(state) {
        return state.rooms;
    },
    getRoom: (state) => (id) => {
        return state.rooms.find(item => item.id == id);
    }
}
const mutations = {
    fetchRoomss(state, header_config) {
        axios.get(URL_API + 'api/room2s', {
            headers: {
                ...header_config,
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
    postRoom(state, data) {
        axios.post(URL_API + 'api/room/create',
            data.room, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putRoom(state, data) {
        axios.put(URL_API + 'api/room/edit/' + data.room.id,
            data.room, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    deleteRoom(state, data) {
        axios.delete(URL_API + 'api/room/delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch();
    }
}

const actions = {
    fetchRoomss({ commit, rootState }) {
        commit('fetchRoomss', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postRoom({ commit, rootState }, room) {
        commit('postRoom', {
            room, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putRoom({ commit, rootState }, room) {
        commit('putRoom', {
            room, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteRoom({ commit, rootState }, id) {
        commit('deleteRoom', {
            id, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        })
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}