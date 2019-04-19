import axios from 'axios'
import { URL_API } from '../config'

const state = {
    producttypes: []
}
const getters = {
    getProductTypess(state) {
        return state.producttypes;
    },
    getProductType: (state) => (id) => {
        return state.producttypes.find(item => item.id == id);
    }
}
const mutations = {
    fetchProductTypess(state, header_config) {
        axios.get(URL_API + 'api/product2types', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.producttypes = res.data;
            }
            else {
                state.producttypes = [];
            }
        });
    },
    postProductType(state, data) {
        axios.post(URL_API + 'api/product2type/create',
            data.producttype, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putProductType(state, data) {
        axios.put(URL_API + 'api/product2type/edit/' + data.producttype.id,
            data.producttype, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    deleteProductType(state, data) {
        axios.delete(URL_API + 'api/product2type/delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch();
    }
}

const actions = {
    fetchProductTypess({ commit, rootState }) {
        commit('fetchProductTypess', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postProductType({ commit, rootState }, producttype) {
        commit('postProductType', {
            producttype, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putProductType({ commit, rootState }, producttype) {
        commit('putProductType', {
            producttype, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteProductType({ commit, rootState }, id) {
        commit('deleteProductType', {
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