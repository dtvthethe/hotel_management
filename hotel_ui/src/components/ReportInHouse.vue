<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>In-House List</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
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
          <tr :key="item.id" v-for="(item, index) in getInHouse">
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
  name: "ReportInHouse",
  data() {
    return {
    };
  },
  computed: {
    ...mapGetters({getInHouse:"getInHouse"}),
  },
  methods: {
    ...mapActions({fetchInHouse:"fetchInHouse"}),
  },
  mounted: function() {
    this.fetchInHouse();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
