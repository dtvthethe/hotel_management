import axios from 'axios'
import { URL_API } from '../config'

const state = {
    invoices: [],
    id_invoice: null
}

const getters = {
    getInvoices(state) {
        return state.invoices;
    },
    getInvoiceID(state) {
        return state.id_invoice;
    },
}

const mutations = {
    setInvoiceID(state, id) {
        state.id_invoice = id;
    },
    setInvoicesToNull(state) {
        state.invoices = [];
    },
    fetchInvoices(state, data) {
        axios.get(URL_API + 'api/invoices?invoice_id=' + data.booking_guest.invoice_id, {
            headers: {
                ...data.header_config
            }
        }).then(res => {
            if (res.status == 200) {
                state.invoices = res.data.map(invoice => {
                    if (invoice.folio_transfer_roomcharge != null && invoice.folio_transfer_minibarcharge == null) {
                        invoice.invoices = invoice.invoices.map(item => {
                            if(item.product.id == 1 || state.id_invoice == invoice.id){
                                return {
                                    ...item,
                                    isShow:true
                                }
                            }
                            else{
                                return {
                                    ...item,
                                    isShow:false
                                }
                            }
                        });
                    }
                    else if (invoice.folio_transfer_roomcharge == null && invoice.folio_transfer_minibarcharge != null) {
                        invoice.invoices = invoice.invoices.map(item => {
                            if(item.product.id != 1 || state.id_invoice == invoice.id){
                                return {
                                    ...item,
                                    isShow:true
                                }
                            }
                            else{
                                return {
                                    ...item,
                                    isShow:false
                                }
                            }
                        });
                    }
                    else{
                        invoice.invoices = invoice.invoices.map(item => {
                            return {
                                ...item,
                                isShow:true
                            }
                        });
                    }
                    return invoice;
                });
            }
            else {
                state.invoices = [];
            }
        });
    },
    fetchInvoiceDetails(state, data) {
        if (data.guest_booking == null) {
            state.invoices = [];
            state.id_invoice = null;
        }
        else {
            axios.get(URL_API + 'api/invoices?booking_id=' + data.guest_booking.booking_id + '&guest_id=' + data.guest_booking.guest_id, {
                headers: {
                    ...data.header_config
                }
            }).then(res => {
                if (res.status == 200) {
                    state.id_invoice = res.data.find(item => (item.booking.id == data.guest_booking.booking_id && item.guest.id == data.guest_booking.guest_id)).id;

                    state.invoices = res.data.map(invoice => {
                        if (invoice.folio_transfer_roomcharge != null && invoice.folio_transfer_minibarcharge == null) {
                            invoice.invoices = invoice.invoices.map(item => {
                                if(item.product.id == 1 || state.id_invoice == invoice.id){
                                    return {
                                        ...item,
                                        isShow:true
                                    }
                                }
                                else{
                                    return {
                                        ...item,
                                        isShow:false
                                    }
                                }
                            });
                        }
                        else if (invoice.folio_transfer_roomcharge == null && invoice.folio_transfer_minibarcharge != null) {
                            invoice.invoices = invoice.invoices.map(item => {
                                if(item.product.id != 1 || state.id_invoice == invoice.id){
                                    return {
                                        ...item,
                                        isShow:true
                                    }
                                }
                                else{
                                    return {
                                        ...item,
                                        isShow:false
                                    }
                                }
                            });
                        }
                        else{
                            invoice.invoices = invoice.invoices.map(item => {
                                return {
                                    ...item,
                                    isShow:true
                                }
                            });
                        }
                        return invoice;
                    });
                }
                else {
                    state.invoices = [];
                    state.id_invoice = null;
                }
            });
        }
    },
    postInvoiceDetail: function (state, data) {
        axios.post(URL_API + 'api/invoicedetail/create',
            data.invoice_detail
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    updateInvoiceDetail: function (state, data) {
        axios.put(URL_API + 'api/invoicedetail/update/' + data.invoice_detail.id,
            data.invoice_detail.data
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch();
    },
    updateInvoiceDetailPriceConfirm: function (state, data) {
        axios.put(URL_API + 'api/invoicedetailprice/update/' + data.invoice_detail.id,
            data.invoice_detail
            , {
                headers: {
                    ...data.header_config
                }
            }).then().catch()
    },
    deleteInvoiceDetail(state, data) {
        axios.delete(URL_API + 'api/invoicedetail/delete/' + data.id, {
            headers: {
                ...data.header_config,
            }
        }).then().catch()
    }
}

const actions = {
    setInvoiceID({ commit }, id) {
        commit('setInvoiceID', id);
    },
    setInvoicesToNull({ commit }) {
        commit('setInvoicesToNull');
    },
    fetchInvoices({ commit, rootState }, booking_guest) {
        commit('fetchInvoices', {
            booking_guest,
            header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    fetchInvoiceDetails({ commit, rootState }, guest_booking) {
        commit('fetchInvoiceDetails', {
            guest_booking,
            header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    postInvoiceDetail({ commit, rootState }, invoice_detail) {
        commit('postInvoiceDetail', {
            invoice_detail, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateInvoiceDetail({ commit, rootState }, invoice_detail) {
        commit('updateInvoiceDetail', {
            invoice_detail, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    updateInvoiceDetailPriceConfirm({ commit, rootState }, invoice_detail) {
        commit('updateInvoiceDetailPriceConfirm', {
            invoice_detail, header_config: {
                'Authorization': 'jwt ' + rootState.user_module.tokenAuth,
            }
        });
    },
    deleteInvoiceDetail({ commit, rootState }, id) {
        commit('deleteInvoiceDetail', {
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
