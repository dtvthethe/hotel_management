import axios from 'axios'
import { URL_API } from '../config'

const state = {
    products: [],
}

const getters = {
    getProducts(state) {
        return state.products;
    }
}

const mutations = {
    fetchProducts() {
        axios.get(URL_API + 'api/products').then(res => {
            if (res.status == 200) {
                state.products = res.data;
            }
            else {
                state.products = [];
            }
        });
    }
}

const actions = {
    fetchProducts({commit}){
        commit('fetchProducts');
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}