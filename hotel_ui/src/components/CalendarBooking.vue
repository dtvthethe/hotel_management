<template>
  <div id="calendar-booking" ref="tbbooking" @click="disableMenuContext">
    <p>{{select_date}}</p>
    <div class="table-reveration noselect">
      <div class="tbheader">
        <div class="tbcell">Rooms / Dates</div>
        <div class="tbcell" :key="dat_index" v-for="(dat, dat_index) in getDays">{{dat.date_format}}</div>
      </div>
      <div class="tbrow" :key="room_index" v-for="(room, room_index) in room_list">
        <div class="tbcell" :style="{width: (windowWidth/numberOfColumn)+'px'}">{{room.name}}</div>
        <div
          class="tbcell tbcell-booking"
          oncontextmenu="return false"
          :data-index="dat_index1"
          :data-room-id="room_index"
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
            :class="item.room_status == 1 ? 'check-in' : item.room_status == 2 ? 'in-house': 'check-out'"
            :data-id="item.id"
            :key="item.id"
            :style="{width: ((windowWidth/numberOfColumn)*item.length)-4 +'px',marginLeft: (windowWidth/numberOfColumn)*item.left+'px'}"
          >{{item.id + ' | '+ item.guest_name + ' | ' + item.client_name}}</button>
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
          data-toggle="modal"
          data-target="#myModal"
          class="list-group-item"
          :key="index"
          v-for="(item, index) in context_menu_list"
        >
          <i :class="item.icon"></i>
          {{item.label}}
        </li>
      </ul>
    </div>
    <!-- //Menu Context -->
    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <header class="panel-heading">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title" id="myModalLabel">Modal title</h4>
          </header>
          <div class="panel-body">
            <div class="">
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
import { parse, differenceInDays, addDays, format } from "date-fns";
import { mapGetters } from "vuex";
import FrmBookingDetail from "./FrmBookingDetail";

export default {
  name: "CalendarBooking",
  data: function() {
    return {
      instance_date: {
        start: parse("2019/03/11"),
        stop: parse("2019/03/17")
      },
      select_date: {
        start: parse("2019/03/11"),
        stop: parse("2019/03/17")
      },
      room_list: [
        {
          id: 12,
          name: "201"
        },
        {
          id: 13,
          name: "202"
        },
        {
          id: 14,
          name: "203"
        },
        {
          id: 15,
          name: "200"
        },
        {
          id: 16,
          name: "204"
        },
        {
          id: 17,
          name: "205"
        },
        {
          id: 18,
          name: "206"
        },
        {
          id: 19,
          name: "207"
        }
      ],
      booking_list: [
        {
          id: 23,
          guest_name: "Ng Van A 11 - 14",
          from: parse("2019/03/11"),
          to: parse("2019/03/14"),
          client_name: "Booking.com",
          room_status: 2,
          id_room: 13,
          left: 1,
          length: 1
        },
        {
          id: 24,
          guest_name: "Hanie 14 - 16",
          from: parse("2019/03/14"),
          to: parse("2019/03/16"),
          client_name: "Agoda",
          room_status: 2,
          id_room: 14,
          left: 1,
          length: 1
        },
        {
          id: 26,
          guest_name: "Abuluxu mu jjjj jj j j jjjj j jjjj 16-18",
          from: parse("2019/03/16"),
          to: parse("2019/03/18"),
          client_name: "Walk-in",
          room_status: 1,
          id_room: 12,
          left: 1,
          length: 1
        },
        {
          id: 27,
          guest_name: "Den truoc 2-17",
          from: parse("2019/03/02"),
          to: parse("2019/03/17"),
          client_name: "Expedia",
          room_status: 3,
          id_room: 16,
          left: 1,
          length: 1
        },
        {
          id: 28,
          guest_name: "Hai dau 11-18",
          from: parse("2019/03/11"),
          to: parse("2019/03/18"),
          client_name: "Booking.com",
          room_status: 2,
          id_room: 17,
          left: 1,
          length: 1
        },
        {
          id: 29,
          guest_name: "Den sau 12-20",
          from: parse("2019/03/12"),
          to: parse("2019/03/20"),
          client_name: "Agoda",
          room_status: 2,
          id_room: 18,
          left: 1,
          length: 1
        },
        {
          id: 30,
          guest_name: "Vo cuc 3/1-22/4",
          from: parse("2019/01/03"),
          to: parse("2019/04/22"),
          client_name: "Booking.com",
          room_status: 1,
          id_room: 15,
          left: 1,
          length: 1
        },
        {
          id: 31,
          guest_name: "Mot tt tt hh hh",
          from: parse("2019/03/13"),
          to: parse("2019/03/13"),
          client_name: "Boo",
          room_status: 3,
          id_room: 19,
          left: 1,
          length: 1
        }
      ],
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
    FrmBookingDetail
  },
  watch: {
    isMenuBar: function(oldIsMenuBar) {
      // this.handleWindowResize();
      // console.log(oldIsMenuBar, newIsMenuBar);
      if (oldIsMenuBar) {
        this.windowWidth = this.windowWidth - this.widthMenuBar;
      } else {
        this.windowWidth = this.windowWidth + this.widthMenuBar;
      }

      // this.windowWidth  = this.$refs.tbbooking.getBoundingClientRect().width;
    }
  },
  computed: {
    ...mapGetters({ isMenuBar: "isMenuBar", widthMenuBar: "widthMenuBar" }),
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
    }
  },
  methods: {
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
        this.contextMenuLeft = event.clientX;
        this.contextMenuTop = event.clientY;
        this.context_menu_visible = !this.context_menu_visible;
        this.context_menu_list = [
          {
            label: "New Reveration",
            icon: "fa fa-pencil"
          }
        ];
      }
    },
    showContextMenuOnButton: function(event) {
      if (event.which === 1) {
        this.context_menu_visible = false;
      }
      if (event.which === 3) {
        this.contextMenuLeft = event.clientX;
        this.contextMenuTop = event.clientY;
        this.context_menu_visible = !this.context_menu_visible;
        this.context_menu_list = [
          {
            label: "Detail",
            icon: "fa fa-pencil"
          },
          {
            label: "Check-in",
            icon: "fa fa-pencil"
          },
          {
            label: "Check-out",
            icon: "fa fa-pencil"
          }
        ];
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
      this.booking_list.forEach(item => {
        if (item.id_room === roomId) {
          let offsetLeft = 1;
          let widthProgressBar = 1;
          let diffStart = differenceInDays(item.from, this.instance_date.start);
          let diffStop = differenceInDays(item.to, this.instance_date.stop);

          // debugger;
          if (diffStart >= 0 && diffStop <= 0) {
            offsetLeft = diffStart + 1;
            widthProgressBar = differenceInDays(item.to, item.from);
          } else {
            if (diffStart <= 0 && diffStop <= 0) {
              offsetLeft = 1;
              widthProgressBar =
                differenceInDays(item.to, item.from) +
                differenceInDays(item.from, this.instance_date.start);
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
    }
  },
  mounted: function() {
    this.windowWidth = this.$refs.tbbooking.getBoundingClientRect().width;
    window.addEventListener("resize", this.handleWindowResize);
    this.numberOfColumn = this.getDays.length + 1;
  },
  beforeDestroy: function() {
    window.removeEventListener("resize", this.handleWindowResize);
  }
};
</script>

<style scoped>
.check-in {
  background-color: green;
}
.check-out {
  background-color: purple;
}
.in-house {
  background-color: #56563d;
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
