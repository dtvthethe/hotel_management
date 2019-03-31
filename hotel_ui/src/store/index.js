import Vue from 'vue'
import Vuex from 'vuex'
import VuejsDialog from 'vuejs-dialog'
import ui_module from './modules/ui_module'
import booking_module from './modules/booking_module'
import frontdesk_module from './modules/frontdesk_module'
import reveration_module from './modules/reveration_module'
import ChangeRoomPopupConfirm from '../components/ChangeRoomPopupConfirm'

import 'vuejs-dialog/dist/vuejs-dialog.min.css';

let dialogOptions = {
    html: false, // set to true if your message contains HTML tags. eg: "Delete <b>Foo</b> ?"
    loader: false, // set to true if you want the dailog to show a loader after click on "proceed"
    reverse: true, // switch the button positions (left to right, and vise versa)
    okText: 'Save',
    cancelText: 'Close',
    animation: 'zoom', // Available: "zoom", "bounce", "fade"
    // type: 'basic', // coming soon: 'soft', 'hard'
};


Vue.use(Vuex);
Vue.use(VuejsDialog,dialogOptions)

Vue.dialog.registerComponent('CHANGE_ROOM_POPUP_CONFIRM', ChangeRoomPopupConfirm);

export default new Vuex.Store({
    modules: {
        ui_module,
        booking_module,
        frontdesk_module,
        reveration_module
    }
});