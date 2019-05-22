<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Guest Leger</h3>
      <div class="toolbar"></div>
    </header>
    <div class="tool-co">
      <table>
        <tr>
          <td><input id="chkisFilterDate" type="checkbox" v-model="filter_field.isFilterDate"> <label for="chkisFilterDate">Is Filter Date</label></td>
          <td>⎨Arrive Date:</td>
          <td>
            <Datepicker
              id="dt-from-date"
              format="dd/MM/yyyy"
              :disabled="!filter_field.isFilterDate"
              v-model="filter_field.arrive_date"
              :disabledDates="{from: this.filter_field.depart_date}"
            ></Datepicker>
          </td>
          <td>Depart Date:</td>
          <td>
              <Datepicker
              id="dt-to-date"
              format="dd/MM/yyyy"
              :disabled="!filter_field.isFilterDate"
              v-model="filter_field.depart_date"
              :disabledDates="{to: this.filter_field.arrive_date}"
            ></Datepicker>
          </td>
          <td>⎬</td>
        </tr>
      </table>
      Booking ID: <input type="text" v-model="filter_field.booking_id">
      &nbsp;&nbsp;&nbsp;Fullname: <input type="text" v-model="filter_field.fullname">
      &nbsp;&nbsp;&nbsp;Client: <select v-model="filter_field.client">
              <option value="0">All</option>
              <option :key="item.id" :value="item.id" v-for="item in getClients">{{item.name}}</option>
            </select>&nbsp;&nbsp;&nbsp;
      <input type="button" value="Search" class="btn btn-info btn-sm" style="margin-bottom: 12px" @click="onClickSearch">
      
    </div>
    <div class="bg-white">
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Booking ID</th>
            <th>Room</th>
            <th>Client</th>
            <th>Full Name</th>
            <th>Date of Arrival</th>
            <th>Date of Depart</th>
            <th>Booking Status</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr :key="bk.id" v-for="(bk, index) in formatGuestLeger">
            <td>{{index+1}}</td>
            <td>{{bk.booking_code}}</td>
            <td>{{bk.room.name}}</td>
            <td>{{bk.client.name}}</td>
            <td>{{bk.guests[0].fullname}}</td>
            <td>{{bk.arrive_date | dateFormat('DD/MM/YYYY')}}</td>
            <td>{{bk.depart_date | dateFormat('DD/MM/YYYY')}}</td>
            <td>{{bk.booking_status.name}}</td>
            <td>
              <a data-toggle="modal" data-target="#myModal" style="cursor: pointer;" @click="onCliclView(bk.id)">Show</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Modal -->
    <div
      class="modal fade remove paddingright"
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
</template>

<script>
import Datepicker from "vuejs-datepicker";
import { mapActions, mapGetters } from "vuex";
import { format, parse } from "date-fns";
import FrmBookingDetail from "./FrmBookingDetail";

export default {
  name: "GuestLeger",
  components: {
    Datepicker,
    FrmBookingDetail
  },
  data() {
    return {
      filter_field: {
        booking_id: null,
        arrive_date: null,
        depart_date: null,
        fullname: null,
        client: 0,
        isFilterDate: false,
        data_booking: {
          id: "",
          action_name: "detail"
        }
      }
    };
  },
  computed: {
    ...mapGetters({
      getGuestLeger: "getGuestLeger",
      getClients: "getClients",
      getSessionDate: "getSessionDate"
    }),
    formatGuestLeger() {
      return this.getGuestLeger.map(item => {
        return {
          ...item,
          arrive_date: parse(item.arrive_date),
          depart_date: parse(item.depart_date)
        };
      });
    }
  },
  methods: {
    ...mapActions({
      fetchGuestLeger: "fetchGuestLeger",
      fetchClientList: "fetchClientList",
      fetchGuestBookingDetail: "fetchGuestBookingDetail",
      setFrmType: "setFrmType",
      fetchBookingPayments:"fetchBookingPayments",
      fetchPaymentTypes:"fetchPaymentTypes"
    }),
    onClickSearch() {
      this.fetchGuestLeger({
        ...this.filter_field,
        arrive_date: format(this.filter_field.arrive_date, "YYYY-MM-DD"),
        depart_date: format(this.filter_field.depart_date, "YYYY-MM-DD")
      });
    },
    onCliclView(id) {
      this.data_booking = {
        id: id,
        action_name: "detail"
      };

      let guest_infor = this.getGuestLeger.find(item => item.id == id)
        .guests[0];
      guest_infor.booking.room = guest_infor.booking.room.id;
      guest_infor.booking.client = guest_infor.booking.client.id;

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
        type: "leger",
        method: "edit",
        data_value: format(this.getSessionDate, "YYYY-MM-DD"),
        data:{
          filter_field: this.filter_field,
          arrive_date: format(this.filter_field.arrive_date, "YYYY-MM-DD"),
          depart_date: format(this.filter_field.depart_date, "YYYY-MM-DD")
        },
        guest_id: guest_infor.id
      });
      this.fetchBookingPayments(this.data_booking.id);
    }
  },
  mounted: function() {
    // this.fetchSessionDate();
    this.fetchClientList();
    this.fetchPaymentTypes();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}
</style>
