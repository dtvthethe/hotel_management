<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Night Audit</h3>
      <div class="toolbar"></div>
    </header>
    <div class="bg-white">
      <template v-if="step_number == 0">
        <h3>Begin Night Audit</h3>
        <strong>You need to perform the following procedures to shift a new working date</strong>
        <ul style="margin-left: 29px;">
          <li>Post No Show/Cancel/Check-In for Pending Arrival List </li>
          <li>Post Nightly Charge</li>
          <li>Perform Check Out or Extend Guest Stay for Pending Check Out</li>
        </ul>
      </template>
      <template v-else-if="step_number == 1">
        <strong>There are pending arrival reservations need you to process</strong>
        <table class="table">
          <thead>
            <tr>
              <th>#</th>
              <th>Room</th>
              <th>Full Name</th>
              <th>Date of Arrival</th>
              <th>Date of Depart</th>
              <th>Booking Status</th>
            </tr>
          </thead>
          <tbody>
            <tr :key="bk.id" v-for="(bk, index) in formatNightDataCheckIn" >
              <td>{{index+1}}</td>
              <td>{{bk.room.name}}</td>
              <td>{{bk.guests[0].fullname}}</td>
              <td>{{bk.arrive_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.depart_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.booking_status.name}}</td>
            </tr>
          </tbody>
        </table>
      </template>
      <template v-else-if="step_number == 2">
        <strong>There are pending check-out need you to process</strong>
        <table class="table">
          <thead>
            <tr>
              <th>#</th>
              <th>Room</th>
              <th>Full Name</th>
              <th>Date of Arrival</th>
              <th>Date of Depart</th>
              <th>Booking Status</th>
            </tr>
          </thead>
          <tbody>
            <tr :key="bk.id" v-for="(bk, index) in formatNightDataCheckOut" >
              <td>{{index+1}}</td>
              <td>{{bk.room.name}}</td>
              <td>{{bk.guests[0].fullname}}</td>
              <td>{{bk.arrive_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.depart_date | dateFormat('DD/MM/YYYY')}}</td>
              <td>{{bk.booking_status.name}}</td>
            </tr>
          </tbody>
        </table>
      </template>
      <template v-else>
        <strong>Finish Night Audit</strong>
      </template>
    </div>
    <input type="button" :disabled="disableButtonNext" :value="valueButtonNext" @click="onClickNext">
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex"
import { parse, addDays, format } from "date-fns"

export default {
  name: "NightAudit",
  data() {
    return {
      step_number: 0,
      date_audit : null,
    };
  },
  computed: {
    ...mapGetters({getSessionDate: "getSessionDate", getNightAudit:"getNightAudit"}),
    valueButtonNext(){
      if(this.step_number >= 3){
        return 'Finish';
      }
      else{
        return 'Next ➤';
      }
    },
    disableButtonNext(){
      if(this.step_number > 3){
        return true;
      }
      if(this.step_number == 1 && this.getNightAudit.length > 0){
        if(this.formatNightDataCheckIn.length > 0){
          return true;
        }
      }
      if(this.step_number == 2 && this.getNightAudit.length > 0){
        if(this.getNightAudit.filter(item => item.booking_status.id == 2).length > 0){
          return true;
        }
      }
      return false;
    },
    formatNightDataCheckIn(){
      return this.getNightAudit.filter(item=>{
        if(item.booking_status.id == 1){
          return true;
        }
      }).map(item=>{
        return {
          ...item,
          arrive_date: parse(item.arrive_date),
          depart_date: parse(item.depart_date)
        }
      });
    },
    formatNightDataCheckOut(){
      return this.getNightAudit.filter(item => item.booking_status.id != 3).map(item=>{
        return {
          ...item,
          arrive_date: parse(item.arrive_date),
          depart_date: parse(item.depart_date)
        }
      });
    }
  },
  methods: {
    ...mapActions({fetchNightAudit:"fetchNightAudit", putDateConfig:"putDateConfig"}),
    onClickNext(){
      if(this.step_number  == 0){
        this.fetchNightAudit({isArrive: true, date_f: this.getSessionDate});
      }
      else if(this.step_number == 1){
        this.fetchNightAudit({isArrive: false, date_f: this.getSessionDate});
      }
      else if(this.step_number == 3){
        let dat = addDays(parse(this.getSessionDate), 1);
        this.putDateConfig(format(dat, 'YYYY-MM-DD'));
      }
      this.step_number += 1;
    }
  },
  mounted: function() {
    // this.fetchSessionDate();
    setTimeout(() => {
      this.date_audit = parse(this.getSessionDate);
    }, 1000);
    
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
