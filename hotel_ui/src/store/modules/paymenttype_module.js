import axios from 'axios'
import { URL_API } from '../config'

const state = {
    payment_types: []
}
const getters = {
    getPaymentTypes(state){
        return state.payment_types;
    }
}
const mutations = {
    fetchPaymentTypes(state, header_config){
        axios.get(URL_API + 'api/paymenttypes', {
            headers:{
                ...header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.payment_types = res.data;
            }
            else {
                state.payment_types= [];
            }
        });
    }
}
const actions = {
    fetchPaymentTypes({commit, rootState}){
        commit('fetchPaymentTypes', {
            'Authorization':'jwt '+rootState.user_module.tokenAuth,
        });
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}