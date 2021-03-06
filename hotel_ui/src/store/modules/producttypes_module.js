import axios from 'axios'
import { URL_API } from '../config'

const state = {
    product_types: [],
}

const getters = {
    getProductTypes(state) {
        return state.product_types;
    }
}

const mutations = {
    fetchProductTypes(state, header_config) {
        axios.get(URL_API + 'api/product_types', {
            headers:{
                ...header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.product_types = res.data;
            }
            else {
                state.product_types = [];
            }
        });
    }
}

const actions = {
    fetchProductTypes({commit, rootState}){
        commit('fetchProductTypes', {
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