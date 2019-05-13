import axios from 'axios'
import { URL_API, SESSION_DATE_NAME, EXCHANGE_USD_NAME } from '../config'

const state = {
    data_value:[],
}
const getters = {
    getSessionDate(state){
        if(state.data_value.length > 0){
            return state.data_value.find(iten=>iten.name == SESSION_DATE_NAME).data_value;
        }
        return null;
    },
    getExchangeUSD(state){
        if(state.data_value.length > 0){
            return state.data_value.find(iten=>iten.name == EXCHANGE_USD_NAME).data_value;
        }
        return null;
    }
}
const mutations = {
    fetchSessionDate(state, header_config){
        axios.get(URL_API + 'api/config', {
            headers:{
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.data_value = res.data;
            }
            else {
                state.data_value = [];
            }
        });
    }
}
const actions = {
    fetchSessionDate({commit, rootState}){
        commit('fetchSessionDate', {
            'Authorization':'jwt '+rootState.user_module.tokenAuth,
        });
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}