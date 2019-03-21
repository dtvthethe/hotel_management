const state = {
    enable_menubar: true,
    width_menubar: 0,
}

// getters:
const getters = {
    isMenuBar: function (state) {
        return state.enable_menubar;
    },
    widthMenuBar: function (state) {
        return state.width_menubar;
    }
}

// mutations
const mutations = {
    switchMenuBar: function (state) {
        state.enable_menubar = !state.enable_menubar;
    },
    setWidthMenuBar: function (state, width) {
        state.width_menubar = width
    }
}

// actions:
const actions = {
    switchMenu: function ({ commit }) {
        commit('switchMenuBar');
    },
    setWidthMenu: function ({ commit }, width) {
        commit('setWidthMenuBar', width)
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}