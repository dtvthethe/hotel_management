<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>ROOM STATUS</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <div>
        <div class="col-md-12 col-sm-12">
          <table>
            <tr>
              <td><input type="text"  v-model="name_status_slect" maxlength="100"></td>
              <td><Datepicker id="dt-from-date" format="dd/MM/yyyy" v-model="filterstatus.date_status_filter"></Datepicker></td>
              <td> Room status</td>
              <td>
                <select v-model="id_status_slect">
                  <option :key="rs.id" :value="rs.id" v-for="rs in room_status_filter">{{rs.name}}</option>
                </select>
              </td>
              <td>
                <input type="button" value="Search" @click="btnSearch_CLick">
              </td>
            </tr>
          </table>
          
          
          
          
        </div>
        <div class="col-md-12 col-sm-12">
          <table class="table">
            <thead>
              <tr>
                <th>#</th>
                <th>Room</th>
                <th>Status</th>
                <th>Date of Arrival</th>
                <th>Date of Depart</th>
              </tr>
            </thead>
            <tbody>
              <tr :key="room.id" v-for="(room, index) in filterRooms" :class="room.color_classname" >
                <td>{{index+1}}</td>
                <td>{{room.name}}</td>
                <td>{{room.booking_infor == null ? room.room_status.name : room.booking_infor.booking.booking_status.name}}</td>
                <td>
                  <span v-if="room.booking_infor != null">
                    {{room.booking_infor.booking.arrive_date | dateFormat('DD/MM/YYYY')}}
                  </span>
                </td>
                <td>
                  <span v-if="room.booking_infor != null">
                    {{room.booking_infor.booking.depart_date | dateFormat('DD/MM/YYYY')}}
                  </span>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker"
import { mapActions, mapGetters } from "vuex"
import { format, parse } from "date-fns"

export default {
  name: "RoomStatus",
  components: {
    Datepicker
  },
  data() {
    return {
      room_status_filter:[
        {
          id: 0,
          name:'All'
        },
        {
          id: 1,
          name:'Ready to Reservation'
        },
        {
          id: 2,
          name:'Busy'
        }
      ],
      id_status_slect: 0,
      name_status_slect: null,
      filterstatus:{
        date_status_filter: new Date(),
        name_status: null,
        id_status:0
      }
    };
  },
  computed: {
    ...mapGetters({
      getRooms: "getRooms",
      getBookings: "getBookings",
      getSessionDate: "getSessionDate"
    }),
    filterRooms(){
      return this.getRooms(-1).map(room => {
        let bk = this.getBookings.find(item => item.booking.room == room.id);
        let clname = '';
        if(bk != undefined){
          bk.booking.arrive_date = parse(bk.booking.arrive_date);
          bk.booking.depart_date = parse(bk.booking.depart_date);
          if(bk.booking.booking_status.id == 1){
            clname = 'room-pending-check-in';
          }
          else if(bk.booking.booking_status.id == 2){
            clname = 'room-occupied';
          }
          else{
            clname = 'room-pending-check-out';
          }
          return {
            ...room,
            booking_infor: bk,
            color_classname: clname
          }
        }
        else{
          if(room.room_status.id == 1){
            clname = 'room-dirty';
          }
          else if(room.room_status.id == 2){
            clname = '';
          }
          else{
            clname = 'room-block';
          }
          return {
            ...room,
            booking_infor: null,
            color_classname: clname
          }
        }
      }).filter(item=>{
        if(item.room_status.id == 3){
          return false;
        }
        else{
          return true
        }
      })
      .filter(item => {
        if(this.filterstatus.name_status != null){
          return item.name.includes(this.filterstatus.name_status);
        }
        else{
          return true;
        }
      }).filter(item=>{
        if(item.room_status.id == 3){
          return false;
        }
        if (this.filterstatus.id_status == 1 && item.booking_infor != null){
            return false;
        }
        if(this.filterstatus.id_status == 2 && item.booking_infor == null){
          return false;
        }
        return true;
      });
    }
  },
  methods: {
    ...mapActions({
      fetchBookings: "fetchBookings",
    }),
    btnSearch_CLick(){
      this.fetchBookings(format(this.filterstatus.date_status_filter, 'YYYY-MM-DD'));
      this.filterstatus.name_status = this.name_status_slect;
      this.filterstatus.id_status = this.id_status_slect;
    }
  },
  mounted: function() {
    // this.fetchSessionDate();
    setTimeout(() => {
      // don't delete this area
      // this.fetchRooms();
      // don't delete this area
      // // dont delete this area
      // this.fetchBookings(format(new Date(), "YYYY-MM-DD"));
      // // dont delete this area
    }, 1000);
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}
/* room status */
.room-pending-check-out {
  background-color: #f73557;
}
.room-pending-check-in {
  background-color: #207aff;
}
.room-pending-check-in td{
  color: #ffffff;
}
.room-block {
  background-color: #f73557;
}
.room-block td{
  color: #ffffff;
}
.room-occupied {
  background-color: yellow;
}
.room-dirty {
  background-color: #2a2727;
}
.room-available {
  background-color: #3dc32f;
}
</style>
