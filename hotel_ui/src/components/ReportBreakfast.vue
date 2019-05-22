<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Breakfast List</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      Date: <input type="date" v-model="q_date">&nbsp;&nbsp;&nbsp;
      <input class="btn btn-info btn-sm" type="button" value="View" @click="onViewClick">
      <table class="table">
        <thead>
          <tr>
            <th>#</th>
            <th>Guest Name</th>
            <th>Room Name</th>
            <th>Arrive Date</th>
            <th>Depart Date</th>
            <th>Adult</th>
            <th>Children</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in getBreakfast">
            <td>{{ index + 1 }}</td>
            <td>{{ item.fullname }}</td>
            <td>{{ item.booking.room.name }}</td>
            <td>{{ item.booking.arrive_date | dateFormat('DD/MM/YYYY') }}</td>
            <td>{{ item.booking.depart_date | dateFormat('DD/MM/YYYY') }}</td>
            <td>{{ item.booking.adult }}</td>
            <td>{{ item.booking.child }}</td>
          </tr>
          <tr>
            <td colspan="6" class="text-right"><strong>Adult = {{ numberOfPersonBF.adult }}</strong></td>
            <td class="text-left"><strong>Children = {{ numberOfPersonBF.child }}</strong></td>
          </tr>
          <tr>
            <td colspan="6"></td>
            <td><strong>Total = {{ numberOfPersonBF.sum }}</strong></td>
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
  name: "ReportBreakfast",
  data() {
    return {
      q_date: format(new Date(), 'YYYY-MM-DD')
    };
  },
  computed: {
    ...mapGetters({getBreakfast:"getBreakfast"}),
    numberOfPersonBF(){
      let adult = 0;
      let child = 0;
      let sum = 0;
      this.getBreakfast.forEach(item=>{
        adult += item.booking.adult;
        child += item.booking.child;
        sum += (item.booking.adult + item.booking.child);
      })
      return {
        adult,
        child,
        sum,
      }
    }
  },
  methods: {
    ...mapActions({fetchBreakfast:"fetchBreakfast"}),
    onViewClick(){
      this.fetchBreakfast(this.q_date);
    }
  },
  mounted: function() {
    this.fetchBreakfast(this.q_date);
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
