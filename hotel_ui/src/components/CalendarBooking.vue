<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Calendar Booking</h3>
      <div class="toolbar"></div>
    </header>
    <div id="calendar-booking" ref="tbbooking" @click="disableMenuContext">
      <div class="tool">
        <Datepicker
          id="dt-from-date"
          format="dd/MM/yyyy"
          v-model="date_filter_from"
          :disabledDates="{from: this.date_filter_to}"
        ></Datepicker>
        <Datepicker
          id="dt-to-date"
          format="dd/MM/yyyy"
          v-model="date_filter_to"
          :disabledDates="{to: this.date_filter_from}"
        ></Datepicker>
        <input type="button" value="Search" @click="onClickSearch" />
      </div>
      <div class="table-reveration noselect">
        <div class="tbheader">
          <div class="tbcell">R/D</div>
          <div
            class="tbcell"
            :key="dat_index"
            v-for="(dat, dat_index) in getDays"
          >{{dat.date_format}}</div>
        </div>
        <div class="tbrow" :key="room_index" v-for="(room, room_index) in getRooms(-1)">
          <div class="tbcell" :style="{width: (windowWidth/numberOfColumn)+'px'}">{{room.name}}</div>
          <div
            class="tbcell tbcell-booking"
            oncontextmenu="return false"
            :data-index="dat_index1"
            :data-room-id="room_index"
            :data-id="room.id"
            :data-date="dat.date_data_format"
            :style="{width: (windowWidth/numberOfColumn)+'px'}"
            :key="dat_index1+'0'+room_index"
            :id="dat_index1+'_'+room_index"
            @mousedown="startMarkPoint"
            @mouseup="stopMarkPoint"
            v-for="(dat, dat_index1) in getDays"
          ></div>
          <div class="booking-bar">
            <button
              oncontextmenu="return false"
              @mouseup="showContextMenuOnButton"
              v-for="item in getReverationByRoomId(room.id)"
              :class="item.booking.booking_status.id == 1 ? 'check-in' : item.booking.booking_status.id == 2 ? 'in-house': 'check-out'"
              :data-id="item.id"
              :data-booking-id="item.booking.id"
              :data-booking-status-id="item.booking.booking_status.id"
              :key="item.id"
              :style="{
                maxWidth: (((windowWidth/numberOfColumn)*item.length)-6) <= 0 ? ((windowWidth/numberOfColumn)-6) + 'px' : (((windowWidth/numberOfColumn)*item.length)-6) +'px',
                width: (((windowWidth/numberOfColumn)*item.length)-6) <= 0 ? ((windowWidth/numberOfColumn)-6) + 'px' : (((windowWidth/numberOfColumn)*item.length)-6) +'px',
                marginLeft: ((windowWidth/numberOfColumn)*item.left)+'px', 
                whiteSpace: 'nowrap', 
                overflow: 'hidden',
              }"
            >{{item.id + ' | '+ item.fullname + ' | ' + item.booking.client.name}}</button>
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
        class="modal fade paddingright"
        id="myModal"
        tabindex="-1"
        role="dialog"
        aria-labelledby="myModalLabel"
      >
        <div class="modal-dialog modal-lg" role="document">
          <div class="modal-content">
            <header class="panel-heading">
              <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                <span aria-hidden="true">&times;</span>
              </button>
              <h4 class="modal-title" id="myModalLabel">Modal title</h4>
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
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker"
import { parse, differenceInDays, addDays, format } from "date-fns"
import { mapGetters, mapActions } from "vuex"
import FrmBookingDetail from "./FrmBookingDetail"

export default {
  name: "CalendarBooking",
  data: function() {
    return {
      date_filter:{
        date_from: addDays(new Date(), -2),
        date_to: addDays(new Date(), 4)
      },
      instance_date: {
        start: addDays(new Date(), -2),
        stop: addDays(new Date(), 4)
      },
      select_date: {
        start: null,
        stop: null
      },
      data_booking: {
        id: "",
        action_name: "new"
      },
      filter_data:{
        date_start:null,
        date_end:null,
        type_to_show: 1
      },
      context_menu_list: [],
      windowWidth: 0,
      numberOfColumn: 0,
      mark_date_start: null,
      mark_date_stop: null,
      context_menu_visible: false,
      contextMenuLeft: 0,
      contextMenuTop: 0
    };
  },
  components: {
    FrmBookingDetail,
    Datepicker
  },
  watch: {
    isMenuBar: function(oldIsMenuBar) {
      if (oldIsMenuBar) {
        this.windowWidth = this.windowWidth - this.widthMenuBar;
      } else {
        this.windowWidth = this.windowWidth + this.widthMenuBar;
      }
    }
  },
  computed: {
    ...mapGetters({
      isMenuBar: "isMenuBar",
      widthMenuBar: "widthMenuBar",
      getRooms: "getRooms",
      getGuestBookings: "getGuestBookings",
      getInvoices: "getInvoices",
      getBookingGuestDetail: "getBookingGuestDetail",
      getBookingDetail: "getBookingDetail",
      getSessionDate:"getSessionDate"
    }),
    getInstanceDays: function() {
      return differenceInDays(
        this.instance_date.stop,
        this.instance_date.start
      );
    },
    getDays: function() {
      let dates = [];
      for (let i = 0; i <= this.getInstanceDays; i++) {
        dates.push({
          date_format: format(
            addDays(this.instance_date.start, i),
            "ddd DD/MM"
          ),
          date_data_format: format(
            addDays(this.instance_date.start, i),
            "YYYY/MM/DD"
          )
        });
      }
      return dates;
    },
    date_filter_from: {
      get() {
        return this.date_filter.date_from;
      },
      set(value) {
        this.date_filter.date_from = value;
        this.date_filter.date_to = addDays(value,6)
      }
    },
    date_filter_to: {
      get() {
        return this.date_filter.date_to;
      },
      set(value) {
        this.date_filter.date_to = value;
        this.date_filter.date_from = addDays(value,-6)
      }
    },
  },
  methods: {
    ...mapActions({
      fetchRooms: "fetchRooms",
      fetchGuestBookings: "fetchGuestBookings",
      setBookingDetailDeafault: "setBookingDetailDeafault",
      setBookingRoom: "setBookingRoom",
      setBookingArriveDate: "setBookingArriveDate",
      setBookingDepartDate: "setBookingDepartDate",
      fetchGuestBookingDetail: "fetchGuestBookingDetail",
      deleteReveration: "deleteReveration",
      updateBooking: "updateBooking",
      removeCalendarBooking: "removeCalendarBooking",
      setFrmType: "setFrmType",
      fetchBookingPayments: "fetchBookingPayments",
      fetchPaymentTypes: "fetchPaymentTypes",
      updateBookingCheckIn: "updateBookingCheckIn",
      updateBookingCheckOut: "updateBookingCheckOut",
      fetchInvoiceDetails: "fetchInvoiceDetails",
      fetchSessionDate:"fetchSessionDate",
      setBookingPaymentToNull:"setBookingPaymentToNull",
      setInvoicesToNull:"setInvoicesToNull",
      setInvoiceID:"setInvoiceID"
    }),
    // onSelectDateFilter(event){
    //   if(event == 'from'){
    //     this.date_filter.date_to = addDays(this.date_filter.date_from,6)
    //   }
    //   if(event == 'to'){
    //     this.date_filter.date_from = addDays(this.date_filter.date_to,-6)
    //   }
    // },
    onClickSearch(){
      this.instance_date.start = this.date_filter.date_from;
      this.instance_date.stop = this.date_filter.date_to;
      this.fetchGuestBookings({
        arrive_date: format(this.instance_date.start, "YYYY-MM-DD"),
        depart_date: format(this.instance_date.stop, "YYYY-MM-DD")
      });
    },
    handleWindowResize() {
      this.windowWidth = this.$refs.tbbooking.getBoundingClientRect().width;
    },
    startMarkPoint: function(event) {
      if (event.which === 1) {
        if (this.context_menu_visible) {
          this.context_menu_visible = false;
        }
        let target = event.target.dataset;
        this.mark_date_start = {
          index: parseInt(target.index),
          roomID: parseInt(target.roomId)
        };
        this.select_date.start = target.date;
        this.select_date.stop = target.date;
        this.data_booking.id = target.id;
      }
    },
    overMarkPoint: function(event) {
      if (event.which === 1) {
        let target = event.target.dataset;
        this.mark_date_stop = {
          index: parseInt(target.index),
          roomID: parseInt(target.roomId)
        };
        this.fill_color(this.mark_date_start, this.mark_date_stop);
      }
    },
    stopMarkPoint: function(event) {
      if (event.which === 1) {
        let target = event.target.dataset;
        this.mark_date_stop = {
          index: parseInt(target.index),
          roomID: parseInt(target.roomId)
        };
        this.fill_color(this.mark_date_start, this.mark_date_stop);
        if (
          differenceInDays(parse(target.date), parse(this.select_date.start)) <
          0
        ) {
          let tmp = this.select_date.start;
          this.select_date.start = target.date;
          this.select_date.stop = tmp;
        } else {
          this.select_date.stop = target.date;
        }
      }
      if (
        event.which === 3 &&
        event.target.className.includes("bg-mark-select")
      ) {
        this.contextMenuLeft = event.pageX;
        this.contextMenuTop = event.pageY;
        this.context_menu_visible = !this.context_menu_visible;
        this.context_menu_list = [
          {
            label: "New Reveration",
            icon: "fa fa-pencil",
            alias: "new",
            confirm_popup: false
          }
        ];
      }
    },
    showContextMenuOnButton: function(event) {
      if (event.which === 1) {
        this.context_menu_visible = false;
      }
      if (event.which === 3) {
        this.contextMenuLeft = event.pageX;
        this.contextMenuTop = event.pageY;
        this.context_menu_visible = !this.context_menu_visible;
        this.data_booking.id = event.target.dataset.bookingId;

        switch (event.target.dataset.bookingStatusId) {
          case "1": // check-in
            this.context_menu_list = [
              {
                label: "Detail",
                icon: "fa fa-pencil",
                alias: "detail",
                confirm_popup: false
              },
              {
                label: "Check-in",
                icon: "fa fa-pencil",
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
                label: "Cancel",
                icon: "fa fa-pencil",
                alias: "delete",
                confirm_popup: true
              }
            ];
            break;
          case "2": // occupied
            this.context_menu_list = [
              {
                label: "Detail",
                icon: "fa fa-pencil",
                alias: "detail",
                confirm_popup: false
              },
              {
                label: "Check-out",
                icon: "fa fa-pencil",
                alias: "checkout",
                confirm_popup: true
              },
              {
                icon: "fa fa-expand",
                label: "Change room",
                alias: "change",
                confirm_popup: true
              },
              {
                icon: "fa fa-plus",
                label: "Room charge bill",
                alias: "",
                confirm_popup: true
              },
              {
                icon: "fa fa-plus",
                label: "Extra charge bill",
                alias: "",
                confirm_popup: true
              }
            ];
            break;
          case "3": // check-out => chi nen lam chuc nang nay o phan calendar
            this.context_menu_list = [
              {
                icon: "fa fa-thumbs-down",
                label: "Open Detail",
                alias: "detail",
                confirm_popup: false
              }
            ];
            break;
          default:
            this.context_menu_list = [];
        }
      }
    },
    fill_color: function(start, stop) {
      if (this.mark_date_start == null || this.mark_date_stop == null) return;
      if (start.index > stop.index) {
        let tmp = start;
        start = stop;
        start.roomID = tmp.roomID;
        stop = tmp;
      }
      document.querySelectorAll(".bg-mark-select").forEach(item => {
        item.classList.remove("bg-mark-select");
      });

      for (let i = start.index; i <= stop.index; i++) {
        document
          .getElementById(i + "_" + start.roomID)
          .classList.add("bg-mark-select");
      }
    },
    getReverationByRoomId: function(roomId) {
      let lst = [];
      this.getGuestBookings.forEach(item => {
        if (item.booking.room.id === roomId) {
          let offsetLeft = 1;
          let widthProgressBar = 1;
          let diffStart = differenceInDays(
            item.booking.arrive_date,
            this.instance_date.start
          );
          let diffStop = differenceInDays(
            item.booking.depart_date,
            this.instance_date.stop
          );

          // debugger;
          if (diffStart >= 0 && diffStop <= 0) {
            offsetLeft = diffStart + 1;
            widthProgressBar = differenceInDays(
              item.booking.depart_date,
              item.booking.arrive_date
            );
          } else {
            if (diffStart <= 0 && diffStop <= 0) {
              offsetLeft = 1;
              widthProgressBar =
                differenceInDays(
                  item.booking.depart_date,
                  item.booking.arrive_date
                ) +
                differenceInDays(
                  item.booking.arrive_date,
                  this.instance_date.start
                );
            } else if (diffStart >= 0 && diffStop >= 0) {
              offsetLeft = diffStart + 1;
              widthProgressBar = this.numberOfColumn - 1 - diffStart;
            } else {
              offsetLeft = 1;
              widthProgressBar = this.numberOfColumn - 1;
            }
          }

          lst.push({ ...item, left: offsetLeft, length: widthProgressBar });
        }
      });
      return lst;
    },
    disableMenuContext: function() {
      this.context_menu_visible = false;
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
      this.data_booking.action_name = aliasName;
      if (this.data_booking.action_name == "detail" && this.data_booking.id) {
        let guest_infor = this.getGuestBookings.find(
          item => item.booking.id == this.data_booking.id
        );
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
          type: "ca",
          method: "edit",
          date_start: format(this.instance_date.start, "YYYY-MM-DD"),
          date_stop: format(this.instance_date.stop, "YYYY-MM-DD")
        });
        this.fetchBookingPayments(this.data_booking.id);
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
                this.removeCalendarBooking(this.data_booking.id);
                dialog.close();
              });
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } else if (this.data_booking.action_name == "new") {
        this.setBookingDetailDeafault();
        this.setBookingRoom(this.data_booking.id);
        this.setBookingArriveDate(parse(this.select_date.start));
        this.setBookingDepartDate(addDays(this.select_date.stop, 1));
        this.setBookingPaymentToNull();
        this.setInvoicesToNull();
        this.setInvoiceID(null);
        this.setFrmType({
          type: "ca",
          method: "new",
          date_start: format(this.instance_date.start, "YYYY-MM-DD"),
          date_stop: format(this.instance_date.stop, "YYYY-MM-DD"),
          booking_code: this.genBookingCode()
        });
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
            // on OK click
            setTimeout(() => {
              let booking = this.getGuestBookings.find(
                item => item.id == this.data_booking.id
              ).booking;
              booking.room.id = dialog.data.id;
              let reser = {
                ...booking,
                room: dialog.data.id,
                booking_status: booking.booking_status.id,
                client: booking.client.id
              };
              this.updateBooking(reser).then(() => {
                dialog.close();
              });
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
            let guest_id = this.getGuestBookings.find(
              item => item.booking.id == this.data_booking.id
            ).id;
            this.updateBookingCheckIn({
              booking_id: this.data_booking.id,
              guest_id
            });
            setTimeout(() => {
              this.fetchGuestBookings({
                arrive_date: format(this.instance_date.start, "YYYY-MM-DD"),
                depart_date: format(this.instance_date.stop, "YYYY-MM-DD")
              });
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
              this.fetchGuestBookings({
                arrive_date: format(this.instance_date.start, "YYYY-MM-DD"),
                depart_date: format(this.instance_date.stop, "YYYY-MM-DD")
              });
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      } else {
        return;
      }
    }
  },
  mounted: function() {
    // UI:
    this.numberOfColumn = this.getDays.length + 1;
    window.addEventListener("resize", this.handleWindowResize);

    // Data:
    this.fetchSessionDate();
    this.fetchRooms();
    this.fetchGuestBookings({
      arrive_date: format(this.instance_date.start, "YYYY-MM-DD"),
      depart_date: format(this.instance_date.stop, "YYYY-MM-DD")
    });
    this.fetchPaymentTypes();
    // this.windowWidth = this.$refs.tbbooking.getBoundingClientRect().width;
    setTimeout(() => {
      this.windowWidth = this.$refs.tbbooking.getBoundingClientRect().width;
    }, 1000);
  },
  beforeDestroy: function() {
    window.removeEventListener("resize", this.handleWindowResize);
  }
};
</script>

<style scoped>
.check-in {
  background-color: #27c24c;
}
.check-out {
  background-color: #ff6c60;
}
.in-house {
  background-color: #fcb322;
}

.bg-mark-select {
  background-color: #f9c9be63;
}
.table-reveration {
  display: table;
  /* border-top: 1px solid red; */
  border-left: 1px solid red;
  position: relative;
  width: 100%;
}
.table-reveration .tbheader,
.table-reveration .tbrow {
  display: table-row;
  z-index: 9;
}
.table-reveration .tbcell {
  display: table-cell;
  border-right: 1px solid red;
  border-bottom: 1px solid red;
  z-index: 10;
  cursor: pointer;
}
.table-reveration .tbheader .tbcell {
  border-top: 1px solid red;
}
.table-reveration .tbcell-booking:not(:first-child):hover {
  background-color: #f9c9be36;
}
.table-reveration .booking-bar {
  position: absolute;
  z-index: 7;
  left: 0px;
  width: 100%;
}

.table-reveration .booking-bar button {
  position: absolute;
  z-index: 7;
  left: 0px;
  margin-top: 1px;
  font-size: 12px;
  border: none;
  border-radius: 3px;
  /* background-color: #895b80; */
  color: #fff;
  text-align: left;
}
.noselect {
  -webkit-touch-callout: none; /* iOS Safari */
  -webkit-user-select: none; /* Safari */
  -khtml-user-select: none; /* Konqueror HTML */
  -moz-user-select: none; /* Firefox */
  -ms-user-select: none; /* Internet Explorer/Edge */
  user-select: none; /* Non-prefixed version, currently
                                  supported by Chrome and Opera */
}
</style>
