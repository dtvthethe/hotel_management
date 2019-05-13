import axios from 'axios'
import { URL_API, NAME_TOKEN, NAME_USERNAME, DATA_NAME_FULLNAME, DATA_NAME_AVATAR, DATA_NAME_IDUSER } from '../config'

const state = {
    users: [],
    user: null,
    tokenAuth: null,
    flagSuccess: false,
    user_editor:null,
}

// getters:
const getters = {
    getUsers(state) {
        return state.users;
    },
    getUser: (state) => (id) => {
        return state.users.find(item => item.id == id);
    },
    getUserByUsername(state){
        return state.user;
    },
    getTokenAuth(state) {
        return state.tokenAuth;
    },
    getUserEditor(state) {
        return state.user_editor;
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
    fetchUserbyID(state, header_config) {
        axios.get(URL_API + 'api/person_profile/'+localStorage.getItem(DATA_NAME_IDUSER), {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.user_editor = res.data;
            }
            else {
                state.user_editor = null;
            }
        });
    },
    fetchUserByUsername(state, header_config) {
        axios.get(URL_API + 'api/person_username?username='+localStorage.getItem(NAME_USERNAME), {
            headers: {
                ...header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                let uss = res.data[0];
                if(uss.users == null){
                    let fullname = uss.first_name +' '+ uss.last_name;

                    localStorage.setItem(DATA_NAME_FULLNAME, fullname);
                    localStorage.setItem(DATA_NAME_AVATAR, null);
                    localStorage.setItem(DATA_NAME_IDUSER, uss.id);

                    state.user = {
                        fullname,
                        avatar: null
                    }

                }
                else{
                    let fullname = uss.users.first_name +' '+ uss.users.last_name;

                    localStorage.setItem(DATA_NAME_FULLNAME, fullname);
                    localStorage.setItem(DATA_NAME_AVATAR, uss.users.avatar);
                    localStorage.setItem(DATA_NAME_IDUSER, uss.users.id);
                    state.user = {
                        fullname,
                        avatar: uss.users.avatar
                    }
                }
            }
            else {
                state.user = null;
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
            localStorage.setItem(NAME_USERNAME, data.username);
            state.tokenAuth = res.data.token;
            state.flagSuccess = true;
            
        }).catch(() => {
            state.tokenAuth = null;
            localStorage.removeItem(NAME_TOKEN);
            localStorage.removeItem(NAME_USERNAME);
            state.flagSuccess = false;
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
            localStorage.removeItem(NAME_USERNAME);
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
    putPerson(state, data) {
        axios.put(URL_API + 'api/person/put' + data.data.id,
            data.data,
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    putPersonUpdate(state, data) {
        axios.put(URL_API + 'api/person/update/' + localStorage.getItem(DATA_NAME_IDUSER),
            data.person,
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
    fetchUserByUsername({ commit, rootState }) {
        commit('fetchUserByUsername', {
            'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
        });
    },
    fetchUserbyID({ commit, rootState }) {
        commit('fetchUserbyID', {
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
    putPerson({ commit, rootState }, data) {
        commit('putPerson', {
            data, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putPersonUpdate({ commit, rootState }, person) {
        commit('putPersonUpdate', {
            person, header_config: {
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
    postUserlogin({ commit, rootState }, data) {
        commit('postUserlogin', data);
        if(rootState.user_module.flagSuccess == true){
            commit('fetchUserByUsername', data);
        }
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