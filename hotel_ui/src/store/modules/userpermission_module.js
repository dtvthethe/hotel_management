import axios from 'axios'
import { URL_API } from '../config'

const state = {
    permissions: []
}

// getters:
const getters = {
    getUserPermissions(state) {
        return state.permissions;
    },

}

// mutations
const mutations = {
    fetchUserPermissions(state, header_config) {
        axios.get(URL_API + 'api/userpermissions', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.permissions = res.data;
            }
            else {
                state.permissions = [];
            }
        });
    }
}

// actions:
const actions = {
    fetchUserPermissions({ commit, rootState }) {
        commit('fetchUserPermissions', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}