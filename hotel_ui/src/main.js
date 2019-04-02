import Vue from 'vue'
import App from './App.vue'
import store from './store'
import router from './router'
import VuejsDialog from 'vuejs-dialog'
import VueCurrencyFilter from 'vue-currency-filter'
import VModal from 'vue-js-modal'
import ChangeRoomPopupConfirm from './components/ChangeRoomPopupConfirm'
// import MinibarPopupConfirm from './components/MinibarPopupConfirm'

import 'vuejs-dialog/dist/vuejs-dialog.min.css';


let dialogOptions = {
  html: true, // set to true if your message contains HTML tags. eg: "Delete <b>Foo</b> ?"
  loader: false, // set to true if you want the dailog to show a loader after click on "proceed"
  reverse: true, // switch the button positions (left to right, and vise versa)
  okText: 'Save',
  cancelText: 'Close',
  animation: 'zoom', // Available: "zoom", "bounce", "fade"
  // type: 'basic', // coming soon: 'soft', 'hard'
};

let currencyFilterOption = {
  symbol: 'VND',
  thousandsSeparator: ',',
  fractionCount: 0,
  fractionSeparator: ',',
  symbolPosition: 'back',
  symbolSpacing: true
}

Vue.config.productionTip = false
Vue.use(VuejsDialog, dialogOptions)
Vue.use(VueCurrencyFilter, currencyFilterOption)
Vue.dialog.registerComponent('CHANGE_ROOM_POPUP_CONFIRM', ChangeRoomPopupConfirm);
// Vue.dialog.registerComponent('MINIBAR_POPUP_CONFIRM', MinibarPopupConfirm);
Vue.use(VModal, { componentName: "popup-modal" })


new Vue({
  router,
  store,
  render: h => h(App),
}).$mount('#app')

