<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Guest Leger</h3>
      <div class="toolbar"></div>
    </header>
    <div class="tool">
      Booking ID: <input type="text" v-model="filter_field.booking_id"><br>
      <input id="chkisFilterDate" type="checkbox" v-model="filter_field.isFilterDate">
      Arrive Date: <Datepicker
          id="dt-from-date"
          format="dd/MM/yyyy"
          :disabled="!filter_field.isFilterDate"
          v-model="filter_field.arrive_date"
          :disabledDates="{from: this.filter_field.depart_date}"
        ></Datepicker>
      Depart Date: <Datepicker
          id="dt-to-date"
          format="dd/MM/yyyy"
          :disabled="!filter_field.isFilterDate"
          v-model="filter_field.depart_date"
          :disabledDates="{to: this.filter_field.arrive_date}"
        ></Datepicker>
      
      <br>
      Fullname: <input type="text" v-model="filter_field.fullname"><br>
      Client:
      <select v-model="filter_field.client">
        <option value="0">All</option>
        <option :key="item.id" :value="item.id" v-for="item in getClients">{{item.name}}</option>  
      </select>
      
      <br>
      <input type="button" value="Search" @click="onClickSearch"/>
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
          </tr>
        </thead>
        <tbody>
          <tr :key="bk.id" v-for="(bk, index) in formatGuestLeger" >
              <td>{{index+1}}</td>
              <td>{{bk.booking_code}}</td>
              <td>{{bk.room.name}}</td>
              <td>{{bk.client.name}}</td>
              <td>{{bk.guests[0].fullname}}</td>
              <td>{{bk.arrive_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.depart_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.booking_status.name}}</td>
            </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker"
import { mapActions, mapGetters } from "vuex"
import { format, parse } from "date-fns"

export default {
  name: "GuestLeger",
  components: {
    Datepicker
  },
  data() {
    return {
      filter_field:{
        booking_id:null,
        arrive_date:null,
        depart_date:null,
        fullname:null,
        client:0,
        isFilterDate:false,
      },
    };
  },
  computed: {
    ...mapGetters({getGuestLeger:"getGuestLeger", getClients:"getClients"}),
    formatGuestLeger(){
      return this.getGuestLeger.map(item=>{
        return {
          ...item,
          arrive_date: parse(item.arrive_date),
          depart_date: parse(item.depart_date)
        }
      });
    }
  },
  methods: {
    ...mapActions({fetchGuestLeger:"fetchGuestLeger", fetchClientList:"fetchClientList"}),
    onClickSearch(){
      this.fetchGuestLeger({
        ...this.filter_field,
        arrive_date: format(this.filter_field.arrive_date, 'YYYY-MM-DD'),
        depart_date: format(this.filter_field.depart_date, 'YYYY-MM-DD')
      });
    }
  },
  mounted: function() {
    this.fetchClientList();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
