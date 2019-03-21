import Vue from 'vue';
import Vuex from 'vuex';
import ui_module from './modules/ui_module';

Vue.use(Vuex);

export default new Vuex.Store({
    modules:{
        ui_module
    }
});