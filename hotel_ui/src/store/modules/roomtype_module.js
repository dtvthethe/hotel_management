import axios from 'axios'
import { URL_API } from '../config'

const state = {
    roomtypes: []
}
const getters = {
    getRoomTypess(state) {
        return state.roomtypes;
    },
    getRoomType: (state) => (id) => {
        return state.roomtypes.find(item => item.id == id);
    }
}
const mutations = {
    fetchRoomTypess(state, header_config) {
        axios.get(URL_API + 'api/room2types', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.roomtypes = res.data;
            }
            else {
                state.roomtypes = [];
            }
        });
    },
    postRoomType(state, data) {
        axios.post(URL_API + 'api/room2type/create',
            data.roomtype, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putRoomType(state, data) {
        axios.put(URL_API + 'api/room2type/edit/' + data.roomtype.id,
            data.roomtype, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    deleteRoomType(state, data) {
        axios.delete(URL_API + 'api/room2type/delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch();
    }
}

const actions = {
    fetchRoomTypess({ commit, rootState }) {
        commit('fetchRoomTypess', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postRoomType({ commit, rootState }, roomtype) {
        commit('postRoomType', {
            roomtype, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putRoomType({ commit, rootState }, roomtype) {
        commit('putRoomType', {
            roomtype, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteRoomType({ commit, rootState }, id) {
        commit('deleteRoomType', {
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