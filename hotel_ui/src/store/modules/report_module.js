import axios from 'axios'
import { URL_API } from '../config'
import { parse } from 'date-fns'

const state = {
    pending_checkin:[],
    pending_checkout:[],
    inhouse:[],
    breakfast:[],
    houseskeeping:[],
}

// getters:
const getters = {
    getCheckin(state){
        return state.pending_checkin;
    },
    getCheckout(state){
        return state.pending_checkout;
    },
    getInHouse(state){
        return state.inhouse;
    },
    getBreakfast(state){
        return state.breakfast;
    },
    getHouseSkeeping(state){
        return state.houseskeeping;
    },
}

// mutations
const mutations = {
    fetchCheckin(state, data){
        axios.get(URL_API + 'api/report/pending_checkin?arrive_date=' + data.arrive_date,
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then(res=>{
            if (res.status == 200) {
                let arr = [];

                res.data.forEach(item => {
                    item.booking.arrive_date = parse(item.booking.arrive_date),
                    item.booking.depart_date = parse(item.booking.depart_date)
                    arr.push(item);
                });
                state.pending_checkin = arr;
            }
            else {
                state.pending_checkin = [];
            }
        }).catch();
    },
    fetchCheckout(state, data){
        axios.get(URL_API + 'api/report/pending_checkout?depart_date=' + data.depart_date,
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then(res=>{
            if (res.status == 200) {
                let arr = [];

                res.data.forEach(item => {
                    item.booking.arrive_date = parse(item.booking.arrive_date),
                    item.booking.depart_date = parse(item.booking.depart_date)
                    arr.push(item);
                });
                state.pending_checkout = arr;
            }
            else {
                state.pending_checkout = [];
            }
        }).catch();
    },
    fetchInHouse(state, header_config){
        axios.get(URL_API + 'api/report/in_house',
            {
                headers: {
                    ...header_config,
                }
            }
        ).then(res=>{
            if (res.status == 200) {
                let arr = [];

                res.data.forEach(item => {
                    item.booking.arrive_date = parse(item.booking.arrive_date),
                    item.booking.depart_date = parse(item.booking.depart_date)
                    arr.push(item);
                });
                state.inhouse = arr;
            }
            else {
                state.inhouse = [];
            }
        }).catch();
    },
    fetchBreakfast(state, data){
        axios.get(URL_API + 'api/report/breakfast?q_date='+data.q_date,
            {
                headers: {
                    ...data.header_config,
                }
            }
        ).then(res=>{
            if (res.status == 200) {
                let arr = [];

                res.data.forEach(item => {
                    item.booking.arrive_date = parse(item.booking.arrive_date),
                    item.booking.depart_date = parse(item.booking.depart_date)
                    arr.push(item);
                });
                state.breakfast = arr;
            }
            else {
                state.breakfast = [];
            }
        }).catch();
    },
    // fetchHouseSkeeping(state){
    //     return state.houseskeeping;
    // },
}

// actions:
const actions = {
    fetchCheckin({ commit, rootState }, arrive_date) {
        commit('fetchCheckin', {
            arrive_date,
            header_config: {'Authorization': 'jwt ' + rootState.user_module.tokenAuth},
        });
    },
    fetchCheckout({ commit, rootState }, depart_date) {
        commit('fetchCheckout', {
            depart_date,
            header_config: {'Authorization': 'jwt ' + rootState.user_module.tokenAuth},
        });
    },
    fetchInHouse({ commit, rootState }) {
        commit('fetchInHouse', {'Authorization': 'jwt ' + rootState.user_module.tokenAuth});
    },
    fetchBreakfast({ commit, rootState }, q_date) {
        commit('fetchBreakfast', {
            q_date,
            header_config: {'Authorization': 'jwt ' + rootState.user_module.tokenAuth},
        });
    },
}

export default {
    state,
    getters,
    actions,
    mutations
}