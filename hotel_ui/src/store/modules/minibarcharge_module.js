import axios from 'axios'
import { parse } from 'date-fns'
import { URL_API } from '../config'

const state = {
    minibar_charges: []
}
const getters = {
    getMinibarCharges(state) {
        return state.minibar_charges;
    },
    getMinibarChargeById: (state) => (id) => {
        return state.minibar_charges.find(item => item.id == id);
    }
}
const mutations = {
    fetchMinibarCharges(state, data) {
        axios.get(URL_API + 'api/minibarcharge?booking_id=' + data.booking_id, {
            headers: {
                ...data.header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.minibar_charges = res.data.map(item => {
                    return {
                        ...item,
                        date_order: parse(item.date_order)
                    }
                });
            }
            else {
                state.minibar_charges = [];
            }
        });
    },
    postMinibarCharge(state, data) {
        axios.post(URL_API + 'api/minibarcharge_create',
            data.minibarcharge, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putMinibarCharge(state, data) {
        axios.put(URL_API + 'api/minibarcharge_update/' + data.minibarcharge.id,
            data.minibarcharge.data, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    deleteMinibarCharge(state, data) {
        axios.delete(URL_API + 'api/minibarcharge_delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch()
    }
}
const actions = {
    fetchMinibarCharges({ commit, rootState }, booking_id) {
        commit('fetchMinibarCharges', {
            booking_id, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    postMinibarCharge({ commit, rootState }, minibarcharge) {
        commit('postMinibarCharge', {
            minibarcharge, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putMinibarCharge({ commit, rootState }, minibarcharge) {
        commit('putMinibarCharge', {
            minibarcharge, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteMinibarCharge({ commit, rootState }, id) {
        commit('deleteMinibarCharge', {id, header_config: {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        }})
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}