import axios from 'axios'
import { URL_API, SESSION_DATE_NAME } from '../config'

const state = {
    session_date:[],
}
const getters = {
    getSessionDate(state){
        if(state.session_date.length > 0){
            return state.session_date.find(iten=>iten.name == SESSION_DATE_NAME).session_date;
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
                state.session_date = res.data;
            }
            else {
                state.session_date = [];
            }
        });
    }
}
const actions = {
    fetchSessionDate({commit, rootState}){
        commit('fetchSessionDate', {
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