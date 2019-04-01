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
    fetchProductTypes() {
        axios.get(URL_API + 'api/product_types').then(res => {
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
    fetchProductTypes({commit}){
        commit('fetchProductTypes');
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}