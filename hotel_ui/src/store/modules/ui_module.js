const state = {
    enable_menubar: true,
    width_menubar: 0,
    is_showprice: true
}

// getters:
const getters = {
    isMenuBar: function (state) {
        return state.enable_menubar;
    },
    widthMenuBar: function (state) {
        return state.width_menubar;
    },
    getIsShowPrice: function (state) {
        return state.is_showprice;
    }
}

// mutations
const mutations = {
    switchMenuBar: function (state) {
        state.enable_menubar = !state.enable_menubar;
    },
    setWidthMenuBar: function (state, width) {
        state.width_menubar = width
    },
    switchShowPrice: function (state) {
        state.is_showprice = !state.is_showprice;
    },
}

// actions:
const actions = {
    switchMenu: function ({ commit }) {
        commit('switchMenuBar');
    },
    setWidthMenu: function ({ commit }, width) {
        commit('setWidthMenuBar', width)
    },
    switchShowPrice: function ({ commit }, width) {
        commit('switchShowPrice', width)
    }
}

export default {
    state,
    getters,
    actions,
    mutations
}