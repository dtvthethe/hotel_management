<template>
  <div @click="disableMenuContext">
    <header class="agileits-box-header clearfix">
      <h3>Front Desk</h3>
      <div class="toolbar"></div>
    </header>
    <div class="front-desk">
      <div class="front-desk-group" :key="roomtype.id" v-for="roomtype in getRoomWithTypes">
        <div class="front-desk-title row">
          <strong>{{roomtype.name}}</strong>
        </div>
        <div class="front-desk-body row">
          <div class="col-xs-3 col-md-2 room" :key="room.id" v-for="room in roomtype.rooms">
            <div
              class="room-containt"
              :class="fillColorToRoom(room.id) ? fillColorToRoom(room.id): room.room_status.id == 1 ?'room-odirty' : room.room_status.id == 3 ? 'room-block':'room-available'"
              :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
              :data-booking-id="fillIDBookingToRoom(room.id)"
              :data-room-id="room.id"
              oncontextmenu="return false"
              @mouseup="enableMenuContext"
            >
              <p
                class="room-number"
                :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
                :data-room-id="room.id"
                :data-booking-id="fillIDBookingToRoom(room.id)"
              >{{room.name}}</p>
              <i
                class="fa"
                :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
                :data-room-id="room.id"
                :data-booking-id="fillIDBookingToRoom(room.id)"
                :class="fillColorToRoom(room.id) == 'room-pending-check-in'? 'fa-level-down':fillColorToRoom(room.id) == 'room-pending-check-out'?'fa fa-plane':fillColorToRoom(room.id) =='room-occupied'?'fa-smile-o': room.room_status.id == 1 ? 'fa-tint': room.room_status.id == 3 ?'fa-lock':'fa-check-circle'"
              ></i>
              <p
                class="room-status"
                :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
                :data-room-id="room.id"
                :data-booking-id="fillIDBookingToRoom(room.id)"
              >{{room.room_status.name}}</p>
              <p
                class="guest-name"
                :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
                :data-room-id="room.id"
                :data-booking-id="fillIDBookingToRoom(room.id)"
              >{{fillNameToRoom(room.id)}}</p>
              <p
                class="room-stay"
                :data-room-status="fillIDStatusToRoom(room.id) ? 'bk_'+fillIDStatusToRoom(room.id) : 'rm_'+room.room_status.id"
                :data-room-id="room.id"
                :data-booking-id="fillIDBookingToRoom(room.id)"
              >{{fillDateToRoom(room.id)}}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Menu Context -->
    <div
      class="row context-menu"
      v-show="context_menu_visible"
      :style="{left:contextMenuLeft+'px', top:contextMenuTop+'px'}"
    >
      <ul class="list-group">
        <li
          :data-toggle="item.confirm_popup ? '' : 'modal'"
          :data-target="item.confirm_popup ? '' : '#myModal'"
          class="list-group-item"
          :key="index"
          @click="onContextMenuItemClick(item.alias)"
          v-for="(item, index) in context_menu_list"
        >
          <i :class="item.icon"></i>
          {{item.label}}
        </li>
      </ul>
    </div>
    <!-- //Menu Context -->
    <!-- Modal -->
    <div
      class="modal fade remove paddingright"
      id="myModal"
      tabindex="-1"
      role="dialog"
      aria-labelledby="myModalLabel"
      ref="myModal"
    >
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <header class="panel-heading">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title" id="myModalLabel">Booking Detail</h4>
          </header>
          <div class="panel-body">
            <div class>
              <!-- Form here! -->
              <FrmBookingDetail></FrmBookingDetail>
              <!-- //Form here! -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";
import FrmBookingDetail from "./FrmBookingDetail";
import { parse, isSameDay, format } from "date-fns";

export default {
  name: "FrontDesk",
  components: {
    FrmBookingDetail
  },
  data: function() {
    return {
      context_menu_visible: false,
      contextMenuLeft: 0,
      contextMenuTop: 0,
      context_menu_list: [],
      data_booking: {
        id: "",
        action_name: "new"
      },
      room_selected_id: 0,
      booking_detail: {},
      data_style_booking_field: {
        booking_dates: "&nbsp;",
        class_name: "room-available",
        guest_name: "",
        id_booking: null
      }
    };
  },
  computed: {
    ...mapGetters({
      getRoomWithTypes: "getRoomWithTypes",
      getBookings: "getBookings",
      getRooms: "getRooms",
      getSessionDate: "getSessionDate",
      getInvoices:"getInvoices",
      getBookingGuestDetail:"getBookingGuestDetail",
      getBookingDetail:"getBookingDetail"
    })
  },
  methods: {
    ...mapActions({
      fetchRoomWithTypes: "fetchRoomWithTypes",
      fetchBookings: "fetchBookings",
      fetchGuestBookingDetail: "fetchGuestBookingDetail",
      setBookingDetailDeafault: "setBookingDetailDeafault",
      setBookingRoom: "setBookingRoom",
      deleteReveration: "deleteReveration",
      updateBooking: "updateBooking",
      removeBookings: "removeBookings",
      setFrmType: "setFrmType",
      fetchPaymentTypes: "fetchPaymentTypes",
      fetchBookingPayments: "fetchBookingPayments",
      updateBookingCheckIn: "updateBookingCheckIn",
      updateBookingCheckOut: "updateBookingCheckOut",
      fetchInvoiceDetails:"fetchInvoiceDetails",
      setBookingPaymentToNull:"setBookingPaymentToNull",
      setInvoicesToNull:"setInvoicesToNull",
      setInvoiceID:"setInvoiceID",
      updateRoomStatus:"updateRoomStatus",
      setBookingCode:"setBookingCode"
    }),
    enableMenuContext: function(event) {
      if (event.which === 3) {
        // set item menu context:
        this.bookingId = event.target.dataset.bookingId;
        this.room_selected_id = event.target.dataset.roomId;
        switch (event.target.dataset.roomStatus) {
          case "rm_1": // dirty
            this.context_menu_list = [
              {
                icon: "fa fa-fire-extinguisher",
                label: "Clean Room",
                alias: "clean",
                confirm_popup: true
              }
            ];
            break;
          case "rm_2": // availble
            this.context_menu_list = [
              {
                icon: "fa fa-thumbs-down",
                label: "Post Dirty",
                alias: "dirty",
                confirm_popup: true
              },
              {
                icon: "fa fa-plus",
                label: "New Reveration",
                alias: "new",
                confirm_popup: false
              },
              {
                icon: "fa fa-lock",
                label: "Block",
                alias: "block",
                confirm_popup: true
              }
            ];
            break;
          case "rm_3": // block
            this.context_menu_list = [
              {
                icon: "fa fa-unlock",
                label: "Unblock room",
                alias: "unblock",
                confirm_popup: true
              }
            ];
            break;
          case "bk_1": // check-in
            this.context_menu_list = [
              {
                icon: "fa fa-info-circle",
                label: "Open Detail",
                alias: "detail",
                confirm_popup: false
              },
              {
                icon: "fa fa-sign-in",
                label: "Check-in",
                alias: "checkin",
                confirm_popup: true
              },
              {
                icon: "fa fa-expand",
                label: "Change room",
                alias: "change",
                confirm_popup: true
              },
              {
                icon: "fa fa-times",
                label: "Cancel Booking",
                alias: "delete",
                confirm_popup: true
              }
            ];
            break;
          case "bk_2": // occupied
            this.context_menu_list = [
              {
                icon: "fa fa-info-circle",
                label: "Open Detail",
                alias: "detail",
                confirm_popup: false
              },
              {
                icon: "fa fa-sign-out",
                label: "Check-out",
                alias: "checkout",
                confirm_popup: true
              },
              {
                icon: "fa fa-expand",
                label: "Change room",
                alias: "change",
                confirm_popup: true
              },
            ];
            break;
          // case "bk_3": // check-out => chi nen lam chuc nang nay o phan calendar
          //   this.context_menu_list = [
          //     {
          //       icon: "fa fa-thumbs-down",
          //       label: "Open Detail",
          //       alias: "detail",
          //       confirm_popup:false,
          //     }
          //   ];
          //   break;
          default:
            this.context_menu_list = [];
        }

        this.contextMenuLeft = event.pageX;
        this.contextMenuTop = event.pageY;
        this.context_menu_visible = !this.context_menu_visible;
      }
      if (event.which === 1) {
        this.context_menu_visible = false;
      }
    },
    disableMenuContext: function() {
      this.context_menu_visible = false;
    },
    getOnceBookingToShow: function(roomId) {
      let bookings = this.getBookings.filter(
        item => item.booking.room == roomId
      );
      if (bookings.length > 1) {
        // co 2 booking trong cung  ngay -> 1 bk out 1bk in => out
        let reser = bookings.filter(
          item => item.booking.booking_status.id == 2
        );
        if (reser) {
          // return bk pendding out
          return reser[0];
        } else {
          // ko co bk occupied => 2 check bk pending in
          let resers = bookings.filter(
            item => item.booking.booking_status.id == 1
          );
          if (resers.length == 1) {
            // return bk pending in
            return resers[0];
          } else if (resers.length > 1) {
            // 2 bk => 1 bk by house, 1 bk by day
            //1 : 2 bk same date:
            let bks = resers.filter(
              item =>
                isSameDay(
                  parse(item.booking.arrive_date),
                  parse(item.booking.depart_date)
                ) == true
            );
            if (bks.length == 1) {
              return bks[0];
            } else if (bks.length > 1) {
              return bks[0];
            } else {
              return null;
            }
          } else {
            return null;
          }
        }
      } else if (bookings.length == 1) {
        return bookings[0];
      } else {
        return null;
      }
    },
    fillColorToRoom: function(roomId) {
      let booking = this.getOnceBookingToShow(roomId);
      if (booking) {
        if (booking.booking.booking_status.id == 1) {
          return "room-pending-check-in";
        } else if (booking.booking.booking_status.id == 2) {
          if (isSameDay(booking.booking.depart_date, this.getSessionDate)) {
            return "room-pending-check-out";
          }
          return "room-occupied";
        } else {
          return "";
        }
      } else {
        return null;
      }
    },
    fillNameToRoom: function(roomId) {
      let booking = this.getOnceBookingToShow(roomId);
      if (booking) {
        return booking.fullname;
      } else {
        return "--:--";
      }
    },
    fillIDBookingToRoom: function(roomId) {
      let booking = this.getOnceBookingToShow(roomId);
      if (booking) {
        return booking.booking.id;
      } else {
        return "";
      }
    },
    fillDateToRoom: function(roomId) {
      let booking = this.getOnceBookingToShow(roomId);
      if (booking) {
        return (
          format(parse(booking.booking.arrive_date), "DD/MM") +
          " ~ " +
          format(parse(booking.booking.depart_date), "DD/MM")
        );
      } else {
        return "_";
      }
    },
    fillIDStatusToRoom: function(roomId) {
      let booking = this.getOnceBookingToShow(roomId);
      if (booking) {
        return booking.booking.booking_status.id;
      } else {
        return null;
      }
    },
    genBookingCode(){
      let code = (Math.floor(Math.random() * 99) + 10).toString() + format(new Date(), 'YYYYMMDDHHmmssSSS').toString()
      if(code.length <= 20){
        return code;
      }
      else{
        return code.substring(0, 20);
      }
    },
    onContextMenuItemClick: function(aliasName) {
      this.data_booking = {
        id: this.bookingId,
        action_name: aliasName
      };
      if (this.data_booking.action_name == "detail" && this.data_booking.id) {
        let guest_infor = this.getBookings.find(item => item.booking.id == this.data_booking.id);
        let guest_param = {};
        if (guest_infor.booking.booking_status.id == 1) {
          guest_param = {
            data_booking: this.data_booking,
            guest_booking: null
          };
        } else {
          guest_param = {
            data_booking: this.data_booking,
            guest_booking: {
              booking_id: this.data_booking.id,
              guest_id: guest_infor.id
            }
          };
        }

        this.fetchGuestBookingDetail(guest_param);
        
        this.setFrmType({
          type: "fo",
          method: "edit",
          data_value: format(this.getSessionDate, "YYYY-MM-DD"),
          guest_id: this.getBookings.find(item => item.booking.id == this.data_booking.id).id
        });
        this.fetchBookingPayments(this.data_booking.id);
        // start [
        // this.fetchMinibarCharges(this.data_booking.id);
        // this.fetchRoomCharges(this.data_booking.id);
        // this.fetchMinibarChargeByBooking(this.data_booking.id);
        // this.fetchBookingByMiniAndRoomCharge(this.data_booking.id);
        // end ]

        // fetch invoices + detail:
        // this.fetchInvoiceDetails({booking_id:this.data_booking.id, guest_id});

      } else if (
        this.data_booking.action_name == "delete" &&
        this.data_booking.id
      ) {
        this.$dialog
          .confirm("Do you want to cancel this reservation?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            setTimeout(() => {
              this.deleteReveration(this.data_booking).then(() => {
                this.removeBookings(this.data_booking.id);
                dialog.close();
              });
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } else if (this.data_booking.action_name == "new") {
        let bk_code = this.genBookingCode();
        this.setBookingDetailDeafault();
        this.setBookingRoom(this.room_selected_id);
        this.setBookingPaymentToNull();
        this.setInvoicesToNull();
        this.setInvoiceID(null);
        this.setFrmType({
          type: "fo",
          method: "new",
          data_value: format(this.getSessionDate, "YYYY-MM-DD"),
          booking_code: bk_code
        });
        this.setBookingCode(bk_code);
      } else if (this.data_booking.action_name == "change") {
        this.$dialog
          .confirm(
            { rooms: this.getRooms(-1) },
            {
              loader: true,
              view: "CHANGE_ROOM_POPUP_CONFIRM"
            }
          )
          .then(dialog => {
            let booking = this.getBookings.find(
              item => item.id == this.data_booking.id
            ).booking;
            let booking_data = {
              ...booking,
              room: dialog.data.id,
              booking_status: booking.booking_status.id
            };
            this.updateBooking(booking_data);
            // on OK click
            setTimeout(() => {
              this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } else if (this.data_booking.action_name == "checkin") {
        this.$dialog
          .confirm("Do you want to check-in this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            let guest_id = this.getBookings.find(item => item.booking.id == this.data_booking.id).id;
            
            this.updateBookingCheckIn({booking_id: this.data_booking.id, guest_id});
            setTimeout(() => {
              this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } else if (this.data_booking.action_name == "checkout") {
        this.$dialog
          .confirm("Do you want to check-out this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateBookingCheckOut(this.data_booking.id);
            setTimeout(() => {
              this.fetchRoomWithTypes();
              this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } 
      else if(this.data_booking.action_name == "dirty"){
        this.$dialog
          .confirm("Do you want to post dirty this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateRoomStatus({room_status:1,id:this.room_selected_id});
            setTimeout(() => {
              this.fetchRoomWithTypes();
              // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else if(this.data_booking.action_name == "clean"){
        this.$dialog
          .confirm("Do you want to clean this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateRoomStatus({room_status:2,id:this.room_selected_id});
            setTimeout(() => {
              this.fetchRoomWithTypes();
              // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else if(this.data_booking.action_name == "block"){
        this.$dialog
          .confirm("Do you want to block this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateRoomStatus({room_status:3,id:this.room_selected_id});
            setTimeout(() => {
              this.fetchRoomWithTypes();
              // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else if(this.data_booking.action_name == "unblock"){
        this.$dialog
          .confirm("Do you want to Unblock this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateRoomStatus({room_status:2,id:this.room_selected_id});
            setTimeout(() => {
              this.fetchRoomWithTypes();
              // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else {
        return;
      }
    }
  },
  mounted: function() {
    // this.fetchSessionDate();
    setTimeout(() => {
      this.fetchRoomWithTypes();
      // // dont delete this area
      // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
      // // dont delete this area
      this.fetchPaymentTypes();
    }, 1500);
  }
};
</script>

<style scoped>
/* front desk */
.front-desk-group .front-desk-title {
  border-bottom: 1px solid red;
  margin: 5px 0px;
}

.front-desk-group .front-desk-body {
  margin-right: 0px;
  margin-left: 0px;
}
.front-desk-group .front-desk-body .room {
  margin: 5px 0px;
  padding: 0px 5px;
  font-size: 13px;
}
.room .room-containt {
  /* height: 92px; */
  width: 100%;
  border-radius: 4px;
  border: 1px solid #8873a2;
  color: #fff;
  text-align: center;
  cursor: pointer;
}
.room .room-containt .room-number {
  border-bottom: 1px solid #fff;
  border-bottom-style: dashed;
  padding: 2px 0px;
  font-weight: bold;
}
.room .room-block .room-number {
  border-color: #000;
}
.room .room-containt i {
  font-size: x-large;
  margin: 11px 0px;
}
.room .room-containt .room-status {
  font-size: small;
}
.room .guest-name {
  overflow: hidden;
  width: 100%;
  white-space: nowrap;
}

/* room status */
.room-pending-check-out {
  background-color: #f73557;
}
.room-pending-check-in {
  background-color: #207aff;
}
.room-block {
  background-color: #fff;
  color: #000 !important;
}
.room-occupied {
  background-color: #e9ad07;
}
.room-odirty {
  background-color: #2a2727;
}
.room-available {
  background-color: #3dc32f;
}
/* front desk */
</style>
