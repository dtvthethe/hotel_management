import axios from 'axios'
import { parse } from 'date-fns'
import { URL_API } from '../config'

const state = {
    roomcharges: []
}
const getters = {
    getRoomCharges(state) {
        return state.roomcharges;
    },
    getRoomChargeById: (state) => (id) => {
        return state.roomcharges.find(item => item.id == id);
    }
}
const mutations = {
    fetchRoomCharges(state, data) {
        axios.get(URL_API + 'api/roomcharge?booking_id=' + data.booking_id, {
            headers: {
                ...data.header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.roomcharges = res.data.map(item => {
                    return {
                        ...item,
                        date_charge: parse(item.date_charge),
                        date_session: parse(item.date_session)
                    }
                });
            }
            else {
                state.roomcharges = [];
            }
        });
    },
    postRoomCharge(state, data) {
        axios.post(URL_API + 'api/roomcharge_create',
            data.roomcharge, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putRoomCharge(state, data) {
        axios.put(URL_API + 'api/roomcharge_update_roomrate/' + data.roomcharge.id,
            data.roomcharge.data, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    deleteRoomCharge(state, data) {
        axios.delete(URL_API + 'api/roomcharge_delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch()
    }
}
const actions = {
    fetchRoomCharges({ commit, rootState }, booking_id) {
        commit('fetchRoomCharges', {
            booking_id, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    postRoomCharge({ commit, rootState }, roomcharge) {
        commit('postRoomCharge', {
            roomcharge, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putRoomCharge({ commit, rootState }, roomcharge) {
        commit('putRoomCharge', {
            roomcharge, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteRoomCharge({ commit, rootState }, id) {
        commit('deleteRoomCharge', {
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