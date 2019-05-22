<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>HouseSkeeping</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Room Name</th>
            <th>Room Status</th>
            <th>Reservation Status</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in getRooms(-1)">
            <td>{{ index + 1 }}</td>
            <td>{{ item.name }}</td>
            <td>{{ item.room_status.name }}</td>
            <td>
              <p v-if="getReverationStatus(item.id)">
                {{getReverationStatus(item.id).booking.booking_status.name}}
              </p>
            </td>
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
  name: "ReportHouseSkeeping",
  data() {
    return {
      arrive_date: format(new Date(), 'YYYY-MM-DD')
    };
  },
  computed: {
    ...mapGetters({getRooms:"getRooms", getBookings:"getBookings"}),
  },
  methods: {
    ...mapActions({}),
    getReverationStatus(roomId){
      if (this.getBookings.length == 0){
        return null;
      }
      return this.getBookings.find(item => item.booking.room == roomId);
    },
  },
  mounted: function() {
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
