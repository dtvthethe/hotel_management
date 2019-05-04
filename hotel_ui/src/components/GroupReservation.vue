<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>GROUP REVERATION</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <div>
        <div class="col-md-6 col-sm-12">
          <fieldset>
            <legend class>Booking Infomation</legend>
            <div class="form-group col-md-6">
              <label for="booking-code">Booking Code</label>
              <input type="text" class="form-control m-bot15" id="booking-code" maxlength="20">
            </div>
            <div class="form-group col-md-6">
              <label for="client">Client</label>
              <select class="form-control m-bot15" id="client"></select>
            </div>
            <div class="form-group col-md-6">
              <label for="room-type">Room Type</label>
              <select class="form-control m-bot15" id="room-type"></select>
            </div>
            <div class="form-group col-md-6">
              <label for="room">Room</label>
              <select class="form-control m-bot15" id="room"></select>
            </div>
            <div class="form-group col-md-6">
              <label for="adult">Adult</label>
              <input class="form-control m-bot15" type="number" min="1" max="100" id="adult">
            </div>
            <div class="form-group col-md-3">
              <label for="child">Child</label>
              <input
                class="form-control m-bot15"
                type="number"
                min="1"
                value="1"
                max="100"
                id="child"
              >
            </div>
            <div class="checkbox col-md-3">
              <label>
                <input type="checkbox">
                Breakfast
              </label>
            </div>
            <div class="form-group col-md-6">
              <label for="roomrate">Room Rate</label>
              <input
                class="form-control m-bot15"
                type="number"
                min="0"
                max="999999999999"
                id="roomrate"
              >
            </div>
            <div class="form-group col-md-6">
              <!-- <i>{{ price ? parseInt(price) : 0 | currency }}</i> -->
            </div>
            <div class="form-group col-md-12">
              <label for="note">Note</label>
              <textarea class="form-control" rows="3" id="note" maxlength="500"></textarea>
            </div>
          </fieldset>
        </div>
        <div class="col-md-6 col-sm-12">
          <fieldset>
            <legend class>Stay Infomation</legend>
            <div class="form-group col-md-6">
              <label id="dt-arrive-date">Arrive Date</label>
              <Datepicker id="dt-arrive-date" format="dd/MM/yyyy"></Datepicker>
            </div>
            <div class="form-group col-md-6">
              <label for="dt-depart-date">DepartDate</label>
              <Datepicker id="dt-depart-date" format="dd/MM/yyyy"></Datepicker>
            </div>
            <div class="form-group col-md-12">
              <div class="form-group">
                <label for="night">Night(s)</label>
                <input class="form-control m-bot15" disabled type="number" min="0" id="night">
              </div>
            </div>
          </fieldset>
          <fieldset>
            <legend class>Guest Infomation</legend>
            <div class="form-group col-md-12">
              <label for="fullname">Full Name</label>
              <input type="text" class="form-control m-bot15" id="fullname" maxlength="150">
            </div>
          </fieldset>
          <input type="button" value="Next >>" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Datepicker from "vuejs-datepicker";
import { mapActions, mapGetters } from "vuex";

export default {
  name: "GroupReservation",
  components: {
    Datepicker
  },
  data() {
    return {
      group_guest: {}
        
    };
  },
  computed: {
    ...mapGetters({})
  },
  methods: {
    ...mapActions({})
  },
  mounted: function() {}
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}
</style>
