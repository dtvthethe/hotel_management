import axios from 'axios'
import { parse } from 'date-fns'
import { URL_API } from '../config'

const state = {
    bookingpayments: []
}
const getters = {
    getBookingPayments(state) {
        return state.bookingpayments;
    },
    getBookingPaymentById: (state) => (id) => {
        return state.bookingpayments.find(item => item.id == id);
    }
}
const mutations = {
    fetchBookingPayments(state, data) {
        axios.get(URL_API + 'api/bookingpayment?booking_id=' + data.booking_id, {
            headers: {
                ...data.header_config,
            }
        }).then(res => {
            if (res.status == 200) {
                state.bookingpayments = res.data.map(item => {
                    return {
                        ...item,
                        date_pay: parse(item.date_pay)
                    }
                });
            }
            else {
                state.bookingpayments = [];
            }
        });
    },
    postBookingPayment(state, data) {
        axios.post(URL_API + 'api/bookingpayment_create',
            data.bookingpayment, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch();
    },
    putBookingPayment(state, data) {
        axios.put(URL_API + 'api/bookingpayment_update/' + data.bookingpayment.id,
            data.bookingpayment.data, {
                headers: {
                    ...data.header_config,
                }
            }
        ).then().catch()
    },
    deleteBookingPayment(state, data) {
        axios.delete(URL_API + 'api/bookingpayment_delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch()
    }
}
const actions = {
    fetchBookingPayments({ commit, rootState }, booking_id) {
        commit('fetchBookingPayments', {
            booking_id, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    postBookingPayment({ commit, rootState }, bookingpayment) {
        commit('postBookingPayment', {
            bookingpayment, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    putBookingPayment({ commit, rootState }, bookingpayment) {
        commit('putBookingPayment', {
            bookingpayment, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteBookingPayment({ commit, rootState }, id) {
        commit('deleteBookingPayment', {
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