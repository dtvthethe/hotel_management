<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Pending Check-in</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      Date: <input type="date" v-model="arrive_date">&nbsp;&nbsp;&nbsp;
      <input type="button" class="btn btn-info btn-sm" value="View" @click="onViewClick">
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Guest Name</th>
            <th>Room Name</th>
            <th>Room Rate</th>
            <th>Arrive Date</th>
            <th>Depart Date</th>
            <th>Reservation Status</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in getCheckin">
            <td>{{ index + 1 }}</td>
            <td>{{ item.fullname }}</td>
            <td>{{ item.booking.room.name }}</td>
            <td>{{ item.booking.price_booking | currency}}</td>
            <td>{{ item.booking.arrive_date | dateFormat('DD/MM/YYYY') }}</td>
            <td>{{ item.booking.depart_date | dateFormat('DD/MM/YYYY') }}</td>
            <td>{{ item.booking.booking_status.name }}</td>
          </tr>
        </tbody>
      </table>
    </div>
    
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { format } from "date-fns";

export default {
  name: "ReportPendingCheckin",
  data() {
    return {
      arrive_date: format(new Date(), 'YYYY-MM-DD')
    };
  },
  computed: {
    ...mapGetters({getCheckin:"getCheckin"}),
  },
  methods: {
    ...mapActions({fetchCheckin:"fetchCheckin"}),
    onViewClick(){
      this.fetchCheckin(this.arrive_date);
    }
  },
  mounted: function() {
    this.fetchCheckin(this.arrive_date);
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
