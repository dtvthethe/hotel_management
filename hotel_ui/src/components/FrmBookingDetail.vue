<template>
  <form role="form" id="frmbookingdetail" class="modal-open">
    
        <a class="btn btn-sm btn-default" data-toggle="modal" data-target="#secondModal" >Second modal</a>
        <a class="btn btn-sm btn-default" @click="onAddMiniBarClick">Add</a>
        <a class="btn btn-sm btn-default" @click="show">Show popup</a>
        <a class="btn btn-sm btn-default" @click="show2">Show popup2</a>

    <!-- Nav tabs -->
    <ul class="nav nav-tabs" role="tablist">
      <li role="presentation" class="active">
        <a
          href="#reservation"
          aria-controls="reservation"
          role="tab"
          data-toggle="tab"
        >Reservation Info</a>
      </li>
      <li role="presentation">
        <a href="#extracharge" aria-controls="extracharge" role="tab" data-toggle="tab">Extra Charge</a>
      </li>
      <li role="presentation">
        <a href="#foliodetail" aria-controls="foliodetail" role="tab" data-toggle="tab">Folio Detail</a>
      </li>
    </ul>

    <!-- Tab panes -->
    <div class="tab-content">
      <!-- reservation -->
      <div role="tabpanel" class="tab-pane active" id="reservation">
        <div class="row">
          <div class="col-md-6 col-sm-12">
            <fieldset>
              <legend class>Booking Infomation</legend>
              <div class="form-group col-md-6">
                <label for="booking-code">Booking Code</label>
                <input
                  type="text"
                  class="form-control m-bot15"
                  id="booking-code"
                  maxlength="20"
                  v-model="booking_code"
                >
              </div>
              <div class="form-group col-md-6">
                <label for="client">Client</label>
                <select class="form-control m-bot15" id="client" v-model="client">
                  <option
                    :key="client.id"
                    :value="client.id"
                    v-for="client in getClients"
                  >{{client.name}}</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="room-type">Room Type</label>
                <select
                  class="form-control m-bot15"
                  id="room-type"
                  v-model="roomtype_id"
                  @change="setRoomToNull"
                >
                  <option
                    :key="roomtype.id"
                    :value="roomtype.id"
                    v-for="roomtype in getRoomTypes"
                  >{{roomtype.name}}</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="room">Room</label>
                <select class="form-control m-bot15" id="room" v-model="room">
                  <option
                    :key="room.id"
                    :value="room.id"
                    v-for="room in getRooms(roomtype_id)"
                  >{{room.name}}</option>
                </select>
              </div>
              <div class="form-group col-md-6">
                <label for="adult">Adult</label>
                <input
                  class="form-control m-bot15"
                  type="number"
                  min="1"
                  max="100"
                  v-model="adult"
                  id="adult"
                >
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
                  v-model="child"
                >
              </div>
              <div class="checkbox col-md-3">
                <label>
                  <input type="checkbox" v-model="is_breakfast">
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
                  v-model="price"
                >
              </div>
              <div class="form-group col-md-6">
                <i>{{ price ? parseInt(price) : 0 | currency }}</i>
              </div>
              <div class="form-group col-md-12">
                <label for="note">Note</label>
                <textarea class="form-control" rows="3" id="note" maxlength="500" v-model="note"></textarea>
              </div>
            </fieldset>
          </div>
          <div class="col-md-6 col-sm-12">
            <fieldset>
              <legend class>Stay Infomation</legend>
              <div class="form-group col-md-6">
                <label id="dt-arrive-date">Arrive Date</label>
                <Datepicker
                  id="dt-arrive-date"
                  format="dd/MM/yyyy"
                  @selected="onSelectDateArrive"
                  :disabledDates="disabledDatesArrive"
                  v-model="arrive_date"
                ></Datepicker>
              </div>
              <div class="form-group col-md-6">
                <label for="dt-depart-date">DepartDate</label>
                <Datepicker
                  id="dt-depart-date"
                  format="dd/MM/yyyy"
                  @selected="onSelectDateDepart"
                  :disabledDates="disabledDatesDepart"
                  v-model="depart_date"
                ></Datepicker>
              </div>
              <div class="form-group col-md-12">
                <div class="form-group">
                  <label for="night">Night(s)</label>
                  <input
                    class="form-control m-bot15"
                    disabled
                    type="number"
                    min="0"
                    v-model="durationTwoDate"
                    id="night"
                  >
                </div>
              </div>
            </fieldset>
            <fieldset>
              <legend class>Guest Infomation</legend>
              <div class="form-group col-md-12">
                <label for="fullname">Full Name</label>
                <input
                  type="text"
                  class="form-control m-bot15"
                  id="fullname"
                  maxlength="150"
                  v-model="fullname"
                >
              </div>
            </fieldset>
          </div>
        </div>
      </div>
      <!-- //reservation -->
      <!-- extracharge -->
      <div role="tabpanel" class="tab-pane" id="extracharge">
        <table class="table table-fixed table-minibar">
          <thead>
            <tr>
              <th class="col-md-2">Date</th>
              <th class="col-md-2">Product</th>
              <th class="col-md-2">Quantity</th>
              <th class="col-md-2">Price</th>
              <th class="col-md-2">Total</th>
              <th class="col-md-2">Option</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">johndoe@email.com</td>
              <td class="col-md-2">John</td>
              <td class="col-md-2">Doe</td>
              <td class="col-md-2">
                a
                a
              </td>
            </tr>
          </tbody>
        </table>
      </div>
      <!-- //extracharge -->
      <!-- foliodetail -->
      <div role="tabpanel" class="tab-pane" id="foliodetail">
        <fieldset>
          <legend class>Payment</legend>
          <div class="col-md-12">
            <input type="button" class="btn btn-default" value="Add Payment">
          </div>
          <div class="col-md-10">
            <table class="table table-fixed table-payment">
              <thead>
                <tr>
                  <th class="col-md-2">Date</th>
                  <th class="col-md-2">Product</th>
                  <th class="col-md-2">Quantity</th>
                  <th class="col-md-2">Price</th>
                  <th class="col-md-2">Total</th>
                  <th class="col-md-2">Option</th>
                </tr>
              </thead>
              <tbody>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
                <tr>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">johndoe@email.com</td>
                  <td class="col-md-2">John</td>
                  <td class="col-md-2">Doe</td>
                  <td class="col-md-2">
                    a
                    a
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          <div class="col-md-2">
            <p>
              Balance:
              <i>0</i>
            </p>
          </div>
        </fieldset>

        <fieldset>
          <legend class>All Guest Transactions</legend>
          <button class="btn btn-warning btn-sm">Add Room Charge</button>
          <button class="btn btn-default btn-sm">Folio Tranfer</button>
          <table class="table table-fixed table-transaction">
            <thead>
              <tr>
                <th class="col-md-2">Date</th>
                <th class="col-md-2">Product</th>
                <th class="col-md-2">Quantity</th>
                <th class="col-md-2">Price</th>
                <th class="col-md-2">Total</th>
                <th class="col-md-2">Option</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">johndoe@email.com</td>
                <td class="col-md-2">John</td>
                <td class="col-md-2">Doe</td>
                <td class="col-md-2">
                  a
                  a
                </td>
              </tr>
           
            </tbody>
          </table>
        </fieldset>
      </div>
      <!-- foliodetail -->
    </div>
    <input
      type="button"
      class="btn btn-info"
      data-dismiss="modal"
      value="Submit"
      @click="saveReveration"
    >

    <!-- Modal -->
    <div id="secondModal" class="modal fade col-md-6 col-md-offset-3 second-modal" role="dialog">
      <div class="modal-dialog">
        <!-- Modal content-->
        <div class="modal-content">
          <div class="modal-header">
            <input type="button" class="close" value="×" data-toggle="modal" data-target="#secondModal">
            <h4 class="modal-title">Modal Header</h4>
          </div>
          <div class="modal-body">
            <p>Some text in the modal</p>
          </div>
          <div class="modal-footer">
            <input type="button" class="btn btn-default" value="Close">
          </div>
        </div>
      </div>
    </div>
    <popup-modal name="hello-world" :clickToClose="false">
      <div class="row">
          <div class="form-group col-md-3">
            <label for="producttypeid">Product Type</label>
            <select class="form-control m-bot15" id="producttypeid" v-model="product_type_id">
              <option :key="pro.id" :value="pro.id" v-for="pro in getProductTypes">{{pro.name}}</option>
            </select>
          </div>
          <div class="form-group col-md-3">
            <label for="productid">Product</label>
            <select class="form-control m-bot15" id="productid" v-model="product.id" @change="onProductSelected">
              <option :key="pro.id" :value="pro.id" v-for="pro in filterProducts">{{pro.name}}</option>
            </select>
          </div>
          <div class="form-group col-md-3">
            <label for="price">Price</label>
            <input
                  class="form-control m-bot15"
                  type="number"
                  min="0"
                  max="999999999999"
                  id="price"
                  v-model="product.price"
                >
          </div>
          <div class="form-group col-md-3">
            <label for="productquantity">Quantity</label>
            <input
                  class="form-control m-bot15"
                  type="number"
                  min="1"
                  value="1"
                  max="100"
                  id="productquantity"
                  v-model="product.quantity"
                >
          </div>
        </div>

      <input type="button" value="Save">
      <input type="button" value="Close" @click="hide">

    </popup-modal>
    <popup-modal name="hello-world2" :clickToClose="false">
      hello, world! 2222
      <input type="text" >

      <input type="button" value="Save">
      <input type="button" value="Close" @click="hide2">

    </popup-modal>
  </form>
</template>
<script>

import Datepicker from "vuejs-datepicker"
import { mapGetters, mapActions } from "vuex"
import { differenceInDays, addDays } from "date-fns"

export default {
  name: "FrmBookingDetail",
  components: {
    Datepicker,
  },
  data: function() {
    return {
      disabledDatesArrive: {
        from: null
      },
      disabledDatesDepart: {
        to: null
      },
      durationTwoDate: -1,
      roomtype_id: -1,
      product_type_id:-1,
      product:{
        id : -1,
        quantity: 1,
        price: 0,
      },
    };
  },
  computed: {
    ...mapGetters({
      getBookingDetail: "getBookingDetail",
      getBookingGuestDetail: "getBookingGuestDetail",
      getClients: "getClients",
      getRooms: "getRooms",
      getRoomTypes: "getRoomTypes",
      getFrmType: "getFrmType",
      getProducts: "getProducts",
      getProductTypes: "getProductTypes"
    }),
    booking_code: {
      get() {
        return this.getBookingDetail.booking_code;
      },
      set(value) {
        this.setBookingCode(value);
      }
    },
    adult: {
      get() {
        return this.getBookingDetail.adult;
      },
      set(value) {
        this.setBookingAdult(value);
      }
    },
    child: {
      get() {
        return this.getBookingDetail.child;
      },
      set(value) {
        this.setBookingChild(value);
      }
    },
    note: {
      get() {
        return this.getBookingDetail.note;
      },
      set(value) {
        this.setBookingNote(value);
      }
    },
    arrive_date: {
      get() {
        return this.getBookingDetail.arrive_date;
      },
      set(value) {
        this.setBookingArriveDate(value);
      }
    },
    depart_date: {
      get() {
        return this.getBookingDetail.depart_date;
      },
      set(value) {
        this.setBookingDepartDate(value);
      }
    },
    is_breakfast: {
      get() {
        return this.getBookingDetail.is_breakfast;
      },
      set(value) {
        this.setBookingIsBreakfast(value);
      }
    },
    price: {
      get() {
        return this.getBookingDetail.price_booking;
      },
      set(value) {
        this.setBookingPriceBooking(value);
      }
    },
    client: {
      get() {
        return this.getBookingDetail.client;
      },
      set(value) {
        this.setBookingClient(value);
      }
    },
    room: {
      get() {
        return this.getBookingDetail.room;
      },
      set(value) {
        if (value) {
          this.setBookingRoom(value);
        } else {
          this.setBookingRoom(null);
        }
      }
    },
    fullname: {
      get() {
        return this.getBookingGuestDetail.fullname;
      },
      set(value) {
        this.setFullname(value);
      }
    },
    filterProducts(){
      if(this.product_type_id > 0){
        return this.getProducts.filter(item => item.product_type == this.product_type_id);
      }
      else{
        return [];
      }
    }
  },
  watch: {
    arrive_date(newValue) {
      if (
        this.getBookingDetail.arrive_date &&
        this.getBookingDetail.depart_date
      ) {
        this.durationTwoDate = differenceInDays(
          this.getBookingDetail.depart_date,
          this.getBookingDetail.arrive_date
        );
      } else {
        this.durationTwoDate = -1;
      }
      this.disabledDatesDepart.to = addDays(newValue, 0);
    },
    depart_date(newValue) {
      if (
        this.getBookingDetail.arrive_date &&
        this.getBookingDetail.depart_date
      ) {
        this.durationTwoDate = differenceInDays(
          this.getBookingDetail.depart_date,
          this.getBookingDetail.arrive_date
        );
      } else {
        this.durationTwoDate = -1;
      }
      this.disabledDatesArrive.from = newValue;
    },
    room() {
      if (this.getBookingDetail.room && this.getBookingDetail.room > 0) {
        this.roomtype_id = this.getRooms(-1).find(
          item => item.id == this.getBookingDetail.room
        ).room_type;
      }
    }
  },
  methods: {
    ...mapActions({
      setBookingCode: "setBookingCode",
      setBookingAdult: "setBookingAdult",
      setBookingChild: "setBookingChild",
      setBookingNote: "setBookingNote",
      setBookingArriveDate: "setBookingArriveDate",
      setBookingDepartDate: "setBookingDepartDate",
      setBookingIsBreakfast: "setBookingIsBreakfast",
      setBookingPriceBooking: "setBookingPriceBooking",
      setBookingClient: "setBookingClient",
      setBookingRoom: "setBookingRoom",
      setFullname: "setFullname",
      fetchClientList: "fetchClientList",
      fetchRooms: "fetchRooms",
      fetchRoomTypeList: "fetchRoomTypeList",
      postReveration: "postReveration",
      updateReveration: "updateReveration",
      fetchGuestBookingDetail: "fetchGuestBookingDetail",
      fetchGuestBookings: "fetchGuestBookings",
      fetchBookings: "fetchBookings",
      fetchProducts: "fetchProducts",
      fetchProductTypes: "fetchProductTypes"
    }),
    onSelectDateArrive: function(event) {
      this.disabledDatesDepart.to = event;
    },
    onSelectDateDepart: function(event) {
      this.disabledDatesArrive.from = event;
    },
    setRoomToNull: function() {
      this.setBookingRoom(null);
    },
    saveReveration: function() {
      if (this.getBookingDetail.id > 0 && this.getBookingGuestDetail.id > 0) {
        this.updateReveration();
        if (this.getFrmType.method == "edit") {
          if (this.getFrmType.type == "fo") {
            setTimeout(() => {
              this.fetchBookings(this.getFrmType.session_date);
            }, 2000);
          }
          if (this.getFrmType.type == "ca") {
            setTimeout(() => {
              this.fetchGuestBookings({
                arrive_date: this.getFrmType.date_start,
                depart_date: this.getFrmType.date_stop
              });
            }, 2000);
          }
        }
      } else {
        this.postReveration();
        if (this.getFrmType.method == "new") {
          if (this.getFrmType.type == "fo") {
            setTimeout(() => {
              this.fetchBookings(this.getFrmType.session_date);
            }, 2000);
          }
          if (this.getFrmType.type == "ca") {
            setTimeout(() => {
              this.fetchGuestBookings({
                arrive_date: this.getFrmType.date_start,
                depart_date: this.getFrmType.date_stop
              });
            }, 2000);
          }
        }
      }
    },
    onProductSelected(){
      this.product.price = this.getProducts.find(item => item.id == this.product.id).price;
    },
    onAddMiniBarClick(){},
    show () {
      this.$modal.show('hello-world');
    },
    hide () {
      this.$modal.hide('hello-world');
    },
    show2 () {
      this.$modal.show('hello-world2');
    },
    hide2 () {
      this.$modal.hide('hello-world2');
    }
  },
  mounted() {
    this.fetchClientList();
    this.fetchRooms();
    this.fetchRoomTypeList();
    this.fetchProducts();
    this.fetchProductTypes();
  }
};
</script>



<style>
.table-minibar tbody {
  height: 350px;
}
.table-payment tbody {
  height: 100px;
}
.table-transaction tbody {
  height: 130px;
}
.table-fixed {
  width: 100%;
}
.table-fixed tbody {
  overflow-y: auto;
  width: 100%;
}
.table-fixed thead,
.table-fixed tbody,
.table-fixed tr,
.table-fixed td,
.table-fixed th {
  display: block;
}

.table-fixed tbody td {
  float: left;
}
.table-fixed thead tr th {
  float: left;
}
.table td,
.table > tbody > tr > td {
  padding: 7px !important;
}
.table > thead > tr > th {
  padding: 7px !important;
}
.second-modal {
  height: 200px;
}
</style>
