import axios from 'axios'
import { URL_API } from '../config'

const state = {
    products: [],
}

const getters = {
    getProducts(state) {
        return state.products;
    },
    getProduct: (state) => (id) => {
        return state.products.find(item => item.id == id);
    }
}

const mutations = {
    fetchProducts(state, header_config) {
        axios.get(URL_API + 'api/products', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.products = res.data;
            }
            else {
                state.products = [];
            }
        });
    },
    fetchProductss(state, header_config) {
        axios.get(URL_API + 'api/product2s', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.products = res.data;
            }
            else {
                state.products = [];
            }
        });
    },
    postProduct(state, data) {
        axios.post(URL_API + 'api/product/create',
            data.product, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putProduct(state, data) {
        axios.put(URL_API + 'api/product/edit/' + data.product.id,
            data.product, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    deleteProduct(state, data) {
        axios.delete(URL_API + 'api/product/delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch();
    }
}

const actions = {
    fetchProducts({ commit, rootState }) {
        commit('fetchProducts', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    fetchProductss({ commit, rootState }) {
        commit('fetchProductss', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postProduct({ commit, rootState }, product) {
        commit('postProduct', {
            product, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putProduct({ commit, rootState }, product) {
        commit('putProduct', {
            product, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteProduct({ commit, rootState }, id) {
        commit('deleteProduct', {
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