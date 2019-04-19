import axios from 'axios'
import { URL_API, NAME_TOKEN } from '../config'

const state = {
    users: [],
    tokenAuth: null,
}

// getters:
const getters = {
    getUsers(state) {
        return state.users;
    },
    getUser: (state) => (id) => {
        return state.users.find(item => item.id == id);
    },
    getTokenAuth(state) {
        return state.tokenAuth;
    },
}

// mutations
const mutations = {
    fetchUsers(state, header_config) {
        axios.get(URL_API + 'api/users', {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.users = res.data;
            }
            else {
                state.users = [];
            }
        });
    },
    postUser(state, data) {
        axios.post(URL_API + 'api/user_create',
            data.data, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    postUserlogin(state, data) {
        axios.post(URL_API + 'api/api-token-auth/',
            data
        ).then((res) => {
            localStorage.setItem(NAME_TOKEN, res.data.token);
            state.tokenAuth = res.data.token;
        }).catch(() => {
            state.tokenAuth = null;
            localStorage.removeItem(NAME_TOKEN);
        });
    },
    verifyToken(state, token) {
        axios.post(URL_API + 'api/api-token-verify/',
            token
        ).then((res) => {
            state.tokenAuth = res.data.token;
        }).catch(() => {
            state.tokenAuth = null;
            localStorage.removeItem(NAME_TOKEN);
        });
    },
    putUser(state, data) {
        axios.put(URL_API + 'api/user_update/' + data.data.id,
            data.data,
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    putUserPassword(state, data) {
        axios.put(URL_API + 'api/user_password/' + data.data.id,
            { 'password': data.data.pw },
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    deleteUser(state, data) {
        axios.delete(URL_API + 'api/user_delete/' + data.id,
            {
                headers: {
                    ...data.header_config,
                }
            }).then().catch()
    },
    getTokenfromLocal(state) {
        state.tokenAuth = localStorage.getItem(NAME_TOKEN);
    },
    removeTokenLocal() {
        state.tokenAuth = null;
        localStorage.removeItem(NAME_TOKEN);
    }
}

// actions:
const actions = {
    fetchUsers({ commit, rootState }) {
        commit('fetchUsers', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    postUser({ commit, rootState }, data) {
        commit('postUser', {
            data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putUser({ commit, rootState }, data) {
        commit('putUser', {
            data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putUserPassword({ commit, rootState }, data) {
        commit('putUserPassword', {
            data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteUser({ commit, rootState }, id) {
        commit('deleteUser', {
            id, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    postUserlogin({ commit }, data) {
        commit('postUserlogin', data);
    },
    verifyToken({ commit }, token) {
        commit('verifyToken', token);
    },
    getTokenfromLocal({ commit }) {
        commit('getTokenfromLocal');
    },
    removeTokenLocal({ commit }) {
        commit('removeTokenLocal');
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}