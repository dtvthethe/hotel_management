<template>
  <form role="form" id="frmbookingdetail" class="modal-open">
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
        <a class="btn btn-sm btn-default" @click="show('minibar-popup', 'new')">Add new</a>
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
            <tr :key="item.id" v-for="item in getMinibarCharges">
              <td class="col-md-2">{{item.date_order | dateFormat('DD/MM/YYYY HH:mm:ss')}}</td>
              <td class="col-md-2">{{item.product.name}}</td>
              <td class="col-md-2">{{item.quantity}}</td>
              <td class="col-md-2">{{item.price_confirm | currency }}</td>
              <td class="col-md-2">{{item.price_confirm * item.quantity | currency }}</td>
              <td class="col-md-2">
                <a style="cursor: pointer;" @click="show('minibar-popup', 'edit', item.id)">Edit</a> |
                <a style="cursor: pointer;" @click="deleteMinibar(item.id)">Delete</a>
              </td>
            </tr>
          </tbody>
        </table>
        <p>Total comes to: {{totalPrice | currency}}</p>
      </div>
      <!-- //extracharge -->
      <!-- foliodetail -->
      <div role="tabpanel" class="tab-pane" id="foliodetail">
        <div class="row">
          <fieldset class="col-md-2">
            <legend class>Payment</legend>
            <div>
              <p>{{balanceTotal | currency}}</p>
              <p>{{strFolioTranfer}}</p>
            </div>
          </fieldset>
          <fieldset class="col-md-10">
            <legend class>Payment</legend>
            <div>
              <a
                class="btn btn-sm btn-default"
                @click="showPaymentPopup('payment-popup', 'new')"
              >Add Payment</a>
            </div>
            <div class="col-md-12">
              <table class="table table-fixed table-payment">
                <thead>
                  <tr>
                    <th class="col-md-2">Date</th>
                    <th class="col-md-2">Credit</th>
                    <th class="col-md-2">Payment</th>
                    <th class="col-md-4">Desciption</th>
                    <th class="col-md-2">Option</th>
                  </tr>
                </thead>
                <tbody>
                  <tr :key="item.id" v-for="item in getBookingPayments">
                    <td class="col-md-2">{{item.date_pay | dateFormat('DD/MM/YYYY HH:mm:ss')}}</td>
                    <td class="col-md-2">{{item.credit | currency}}</td>
                    <td class="col-md-2">{{item.payment_type.name}}</td>
                    <td class="col-md-4">{{item.desciption}}</td>
                    <td class="col-md-2">
                      <a
                        style="cursor: pointer;"
                        @click="show('payment-popup', 'edit', item.id)"
                      >Edit</a> |
                      <a
                        style="cursor: pointer;"
                        @click="deleteBookingPaymentClick(item.id)"
                      >Delete</a>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </fieldset>
        </div>
        <div class="row">
          <fieldset class="col-md-12">
            <legend class>All Guest Transactions</legend>
            <a class="btn btn-sm btn-warning" @click="addRoomCharge()">Add Room Charge</a>
            <a
              class="btn btn-sm btn-default"
              :class="{'disabled' : disableButtonByFolioTranferBooking}"
              @click="transferFolio()"
            >Folio Transfer</a>
            <a
              class="btn btn-sm btn-danger"
              :class="{'disabled' : disableButtonByFolioTranferBooking2}"
              @click="cancelTransferFolio()"
            >Cancel Folio Transfer</a>
            <table class="table table-fixed table-transaction">
              <thead>
                <tr>
                  <th class="col-md-2">Date</th>
                  <th class="col-md-1">Room</th>
                  <th class="col-md-3">Product</th>
                  <th class="col-md-2">Price</th>
                  <th class="col-md-1">Quantity</th>
                  <th class="col-md-2">Total</th>
                  <th class="col-md-1">Option</th>
                </tr>
              </thead>
              <tbody>
                <tr :key="item.id" v-for="item in allTransferRoomChargeMinibar">
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.date_order | dateFormat('DD/MM/YYYY HH:mm:ss')}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.room_name}}</td>
                  <td
                    class="col-md-3"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.product_name}}</td>
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.price_confirm | currency}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.quantity}}</td>
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >{{item.total | currency}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':item.type_item == 'room', 'transfer-other-minibar':(item.booking_id != getBookingGuestDetail.id && item.type_item == 'minibar')}"
                  >
                    <span v-if="item.show_option" style="display: inline">
                      <a
                        style="cursor: pointer;"
                        @click="show('roomcharge-popup', 'edit', item.item_id)"
                      >Edit</a> |
                      <a
                        style="cursor: pointer;"
                        @click="deleteRoomChargeClick(item.item_id)"
                      >Delete</a>
                    </span>
                    <span v-else>&emsp;</span>
                  </td>
                </tr>
              </tbody>
            </table>
            <p>Total = {{allTransferRoomChargeMinibarToTal | currency}}</p>
          </fieldset>
        </div>
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

    <!-- minibar popup -->
    <popup-modal name="minibar-popup" :clickToClose="false">
      <div class="row">
        <div class="form-group col-md-3">
          <label for="producttypeid">Product Type</label>
          <select
            class="form-control m-bot15"
            id="producttypeid"
            v-model="product_type_id"
            @change="onProductTypeSelected"
          >
            <option :key="pro.id" :value="pro.id" v-for="pro in getProductTypes">{{pro.name}}</option>
          </select>
        </div>
        <div class="form-group col-md-3">
          <label for="productid">Product</label>
          <select
            class="form-control m-bot15"
            id="productid"
            v-model="minibarcharge.product"
            @change="onProductSelected"
          >
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
            v-model="minibarcharge.price_confirm"
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
            v-model="minibarcharge.quantity"
          >
        </div>
      </div>

      <input type="button" value="Save" @click="onSaveMiniBarClick()">
      <input type="button" value="Close" @click="hide('minibar-popup')">
    </popup-modal>
    <!-- //minibar popup -->

    <!-- popup payment -->
    <popup-modal name="payment-popup" :clickToClose="false">
      Credit:
      <input type="number" v-model="bookingpayment.credit">
      <i>{{bookingpayment.credit | currency}}</i>
      <br>desciption:
      <input type="text" maxlength="200" v-model="bookingpayment.desciption">
      <br>Payment type:
      <select
        class="form-control m-bot15"
        id="paymenttype"
        v-model="bookingpayment.payment_type"
      >
        <option :key="item.id" :value="item.id" v-for="item in getPaymentTypes">{{item.name}}</option>
      </select>
      <input type="button" value="Save" @click="onSavePaymentClick()">
      <input type="button" value="Close" @click="hide('payment-popup')">
    </popup-modal>
    <!--// popup payment -->

    <!-- popup payment -->
    <popup-modal name="roomcharge-popup" :clickToClose="false">
      Room rate:
      <input type="number" v-model="roomcharge.price_confirm">
      <i>{{roomcharge.price_confirm | currency}}</i>
      <br>

      <input type="button" value="Save" @click="onSaveRoomChargeClick()">
      <input type="button" value="Close" @click="hide('roomcharge-popup')">
    </popup-modal>
    <!--// popup payment -->

    <!-- popup foliotransfer -->
    <popup-modal name="foliotransfer-popup" :clickToClose="false">
      Folio ID:
      <input type="text" v-model="folio_transfer.id_folio_transfer">
      <i>{{messageErrorFolioTransfer}}</i>
      <br>
      <div :key="item.id" v-for="item in folio_transfer.typeoffoliotransfers">
        <input
          name="foliotransfer"
          type="radio"
          v-model="folio_transfer.id_folio_transfer_select"
          :value="item.id"
          :id="'foliotransfer-id'+item.id"
        >
        <label :for="'foliotransfer-id'+item.id">{{item.name}}</label>
      </div>

      <input
        type="button"
        value="Save"
        :disabled="messageErrorFolioTransfer"
        @click="onSaveFolioTransferClick()"
      >
      <input type="button" value="Close" @click="hide('foliotransfer-popup')">
    </popup-modal>
    <!--// popup foliotransfer -->
  </form>
</template>
<script>
import Datepicker from "vuejs-datepicker";
import { mapGetters, mapActions } from "vuex";
import { differenceInDays, addDays, format, isSameDay, parse } from "date-fns";

export default {
  name: "FrmBookingDetail",
  components: {
    Datepicker
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
      product_type_id: -1,
      second_popup_status: "",
      minibarcharge: {
        price_confirm: 0,
        quantity: 1,
        booking: 0,
        product: 0
      },
      bookingpayment: {
        credit: 0,
        desciption: null,
        booking: -1,
        payment_type: -1
      },
      roomcharge: {
        price_confirm: 0,
        date_charge: null,
        date_session: null,
        booking: -1
      },
      id_editing: 0,
      folio_transfer: {
        id_folio_transfer: null,
        id_folio_transfer_select: 1,
        typeoffoliotransfers: [
          {
            id: 1,
            name: "All charge"
          },
          {
            id: 2,
            name: "Room charge"
          },
          {
            id: 3,
            name: "Extra charge"
          }
        ]
      }
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
      getProductTypes: "getProductTypes",
      getMinibarCharges: "getMinibarCharges",
      getMinibarChargeById: "getMinibarChargeById",
      getBookingPayments: "getBookingPayments",
      getBookingPaymentById: "getBookingPaymentById",
      getRoomCharges: "getRoomCharges",
      getRoomChargeById: "getRoomChargeById",
      getPaymentTypes: "getPaymentTypes",
      getSessionDate: "getSessionDate",
      getMinibarChargeByBooking: "getMinibarChargeByBooking",
      getBookingByMiniAndRoomCharge: "getBookingByMiniAndRoomCharge"
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
    filterProducts() {
      if (this.product_type_id > 0) {
        return this.getProducts.filter(
          item => item.product_type == this.product_type_id
        );
      } else {
        return this.getProducts;
      }
    },
    totalPrice() {
      let total = 0;
      this.getMinibarCharges.forEach(item => {
        total += item.price_confirm * item.quantity;
      });
      return total;
    },
    disableButtonByFolioTranferBooking() {
      if (this.getBookingDetail.booking_status == 3) {
        return true; // disable
      } else if (this.getBookingByMiniAndRoomCharge.length > 0) {
        return true; // disable
      } else {
        let roomCharge = this.getBookingDetail
          .booking_folio_transfer_roomcharge;
        let minibarCharge = this.getBookingDetail
          .booking_folio_transfer_minibarcharge;
        if (roomCharge == undefined && minibarCharge == undefined) {
          return false;
        } else if (roomCharge == null && minibarCharge == null) {
          return false;
        } else {
          return true;
        }
        // return false;
      }
    },
    disableButtonByFolioTranferBooking2() {
      if (this.getBookingDetail.booking_status == 3) {
        return true; // disable
      } else if (this.getBookingByMiniAndRoomCharge.length > 0) {
        return true; // disable
      } else {
        let roomCharge = this.getBookingDetail
          .booking_folio_transfer_roomcharge;
        let minibarCharge = this.getBookingDetail
          .booking_folio_transfer_minibarcharge;
        if (roomCharge == undefined && minibarCharge == undefined) {
          return true;
        } else if (roomCharge == null && minibarCharge == null) {
          return true;
        } else {
          return false;
        }
      }
    },
    messageErrorFolioTransfer() {
      if (
        this.folio_transfer.id_folio_transfer == this.getBookingGuestDetail.id
      ) {
        return "Can't set to this Folio ID.";
      }
      return null;
    },
    allTransferRoomChargeMinibar() {
      let allRoomChargeMinibars = [];
      // minibar
      if (this.getMinibarChargeByBooking.length > 0) {
        this.getMinibarChargeByBooking.forEach(item => {
          allRoomChargeMinibars.push({
            item_id: item.id,
            booking_id: item.booking.id,
            date_order: item.date_order,
            room_name: item.booking.room.name,
            product_name: item.product.name,
            price_confirm: item.price_confirm,
            quantity: item.quantity,
            total: item.quantity * item.price_confirm,
            type_item: "minibar",
            show_option: false
          });
        });
      }
      // room
      if (this.getRoomCharges.length > 0) {
        this.getRoomCharges.forEach(item => {
          allRoomChargeMinibars.push({
            item_id: item.id,
            booking_id: item.booking.id,
            date_order: item.date_charge,
            room_name: item.booking.room.name,
            product_name: "Room Charge",
            price_confirm: item.price_confirm,
            quantity: 1,
            total: item.price_confirm,
            type_item: "room",
            show_option:
              this.getBookingGuestDetail.id == item.booking.id ? true : false
          });
        });
      }
      return allRoomChargeMinibars;
    },
    allTransferRoomChargeMinibarToTal() {
      let total_folio = 0;
      // minibar
      if (this.getMinibarChargeByBooking.length > 0) {
        this.getMinibarChargeByBooking.forEach(item => {
          total_folio += item.quantity * item.price_confirm;
        });
      }
      // room
      if (this.getRoomCharges.length > 0) {
        this.getRoomCharges.forEach(item => {
          total_folio += item.price_confirm;
        });
      }
      return total_folio;
    },
    balanceTotal() {
      if (this.getBookingGuestDetail.id == undefined) {
        return 0;
      }
      let totalPayment = 0;
      let totalBalance = 0;

      this.getBookingPayments.forEach(item => {
        totalPayment += item.credit;
      });

      if (
        this.getBookingDetail.booking_folio_transfer_minibarcharge == null &&
        this.getBookingDetail.booking_folio_transfer_roomcharge == null
      ) {
        return this.allTransferRoomChargeMinibarToTal - totalPayment;
      } else {
        if (this.getBookingDetail.booking_folio_transfer_roomcharge == null) {
          // room charge
          if (this.getRoomCharges.length > 0) {
            this.getRoomCharges.forEach(item => {
              totalBalance += item.price_confirm;
            });
          }
        }

        if (
          this.getBookingDetail.booking_folio_transfer_minibarcharge == null
        ) {
          // minibar
          if (this.getMinibarChargeByBooking.length > 0) {
            this.getMinibarChargeByBooking.forEach(item => {
              totalBalance += item.quantity * item.price_confirm;
            });
          }
        }
        return totalBalance - totalPayment;
      }
    },
    strFolioTranfer() {
      if (this.getBookingGuestDetail.id == undefined) {
        return 0;
      }
      let iDFolio = 0;
      let strFolio = "";

      if (
        this.getBookingDetail.booking_folio_transfer_minibarcharge == null &&
        this.getBookingDetail.booking_folio_transfer_roomcharge == null
      ) {
        return "";
      } else {
        if (this.getBookingDetail.booking_folio_transfer_roomcharge != null) {
          // room charge
          iDFolio = this.getBookingDetail.booking_folio_transfer_roomcharge;
          strFolio += "Room Charge";
        }

        if (
          this.getBookingDetail.booking_folio_transfer_minibarcharge != null
        ) {
          // minibar
          iDFolio = this.getBookingDetail.booking_folio_transfer_minibarcharge;
          if (strFolio == "") {
            strFolio += "Minibar Charge";
          } else {
            strFolio += ", Minibar Charge";
          }
        }

        return "Folio ID:" + iDFolio + "(" + strFolio + ")";
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
      fetchProductTypes: "fetchProductTypes",
      postMinibarCharge: "postMinibarCharge",
      fetchMinibarCharges: "fetchMinibarCharges",
      putMinibarCharge: "putMinibarCharge",
      deleteMinibarCharge: "deleteMinibarCharge",
      fetchBookingPayments: "fetchBookingPayments",
      postBookingPayment: "postBookingPayment",
      putBookingPayment: "putBookingPayment",
      deleteBookingPayment: "deleteBookingPayment",
      fetchRoomCharges: "fetchRoomCharges",
      postRoomCharge: "postRoomCharge",
      putRoomCharge: "putRoomCharge",
      deleteRoomCharge: "deleteRoomCharge",
      updateBookingFolioTransfer: "updateBookingFolioTransfer",
      fetchMinibarChargeByBooking: "fetchMinibarChargeByBooking"
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
    onProductTypeSelected() {
      this.minibarcharge.price_confirm = 0;
    },
    onProductSelected() {
      this.minibarcharge.price_confirm = this.getProducts.find(
        item => item.id == this.minibarcharge.product
      ).price;
    },
    onSaveMiniBarClick() {
      if (this.second_popup_status == "new") {
        let data = {
          ...this.minibarcharge,
          booking: this.getBookingGuestDetail.id
        };
        this.postMinibarCharge(data);
        setTimeout(() => {
          this.fetchMinibarCharges(this.getBookingGuestDetail.id);
          this.fetchMinibarChargeByBooking(this.getBookingGuestDetail.id);
          this.$modal.hide("minibar-popup");
        }, 2000);
      }
      if (this.second_popup_status == "edit") {
        this.putMinibarCharge({
          data: this.minibarcharge,
          id: this.id_editing
        });
        setTimeout(() => {
          this.fetchMinibarCharges(this.getBookingGuestDetail.id);
          this.fetchMinibarChargeByBooking(this.getBookingGuestDetail.id);
          this.$modal.hide("minibar-popup");
        }, 2000);
      }
    },
    show(popup_name, status, id = 0) {
      if (id > 0) {
        if (popup_name == "minibar-popup") {
          let minidt = this.getMinibarChargeById(id);
          this.id_editing = id;
          this.minibarcharge = {
            price_confirm: minidt.price_confirm,
            quantity: minidt.quantity,
            booking: minidt.booking,
            product: minidt.product.id
          };
          this.product_type_id = minidt.product.product_type;
        }
        if (popup_name == "payment-popup") {
          let bkpayment = this.getBookingPaymentById(id);
          this.id_editing = id;
          this.bookingpayment = {
            credit: bkpayment.credit,
            desciption: bkpayment.desciption,
            booking: bkpayment.booking,
            payment_type: bkpayment.payment_type.id
          };
        }
        if (popup_name == "roomcharge-popup") {
          let roomcharge = this.getRoomChargeById(id);
          this.id_editing = id;
          this.roomcharge = {
            price_confirm: roomcharge.price_confirm,
            date_charge: roomcharge.date_charge,
            date_session: roomcharge.date_session,
            booking: roomcharge.booking
          };
        }
      }
      this.second_popup_status = status;
      this.$modal.show(popup_name);
    },
    hide(popup_name) {
      this.second_popup_status = "";
      this.$modal.hide(popup_name);
    },
    deleteMinibar(id) {
      this.$dialog
        .confirm("Do you want to remove this item?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          this.deleteMinibarCharge(id);

          setTimeout(() => {
            this.fetchMinibarCharges(this.getBookingGuestDetail.id);
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    },
    deleteBookingPaymentClick(id) {
      this.$dialog
        .confirm("Do you want to remove this item?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          this.deleteBookingPayment(id);

          setTimeout(() => {
            this.fetchBookingPayments(this.getBookingGuestDetail.id);
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    },
    deleteRoomChargeClick(id) {
      this.$dialog
        .confirm("Do you want to remove this item?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          this.deleteRoomCharge(id);

          setTimeout(() => {
            this.fetchRoomCharges(this.getBookingGuestDetail.id);
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    },
    onSavePaymentClick() {
      if (this.second_popup_status == "new") {
        let data = {
          ...this.bookingpayment,
          booking: this.getBookingGuestDetail.id
        };
        this.postBookingPayment(data);
        setTimeout(() => {
          this.fetchBookingPayments(this.getBookingGuestDetail.id);
          this.$modal.hide("payment-popup");
        }, 2000);
      }
      if (this.second_popup_status == "edit") {
        this.putBookingPayment({
          data: this.bookingpayment,
          id: this.id_editing
        });
        setTimeout(() => {
          this.fetchBookingPayments(this.getBookingGuestDetail.id);
          this.$modal.hide("payment-popup");
        }, 2000);
      }
    },
    onSaveRoomChargeClick() {
      if (this.second_popup_status == "edit") {
        this.putRoomCharge({
          data: {
            price_confirm:this.roomcharge.price_confirm,
          },
          id: this.id_editing
        });
        setTimeout(() => {
          this.fetchRoomCharges(this.getBookingGuestDetail.id);
          this.$modal.hide("roomcharge-popup");
        }, 2000);
      }
    },
    addRoomCharge() {
      let data = {
        booking: this.getBookingGuestDetail.id,
        price_confirm: this.price,
        date_session: format(this.getSessionDate, "YYYY-MM-DD")
      };
      if (
        this.getRoomCharges.length == 0 ||
        !this.getRoomCharges.find(item =>
          isSameDay(parse(this.getSessionDate), parse(item.date_session))
        )
      ) {
        this.$dialog
          .confirm("Do you want to add room charge?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.postRoomCharge(data);

            setTimeout(() => {
              this.fetchRoomCharges(this.getBookingGuestDetail.id);
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
    },
    showPaymentPopup(popup_name, status) {
      this.second_popup_status = status;
      this.$modal.show(popup_name);
    },
    transferFolio() {
      this.$modal.show("foliotransfer-popup");
    },
    onSaveFolioTransferClick() {
      let data = null;
      if (this.folio_transfer.id_folio_transfer_select == 1) {
        data = {
          booking_folio_transfer_roomcharge: this.folio_transfer
            .id_folio_transfer,
          booking_folio_transfer_minibarcharge: this.folio_transfer
            .id_folio_transfer
        };
        this.updateBookingFolioTransfer({
          id: this.getBookingGuestDetail.id,
          data: data
        });
      } else if (this.folio_transfer.id_folio_transfer_select == 2) {
        data = {
          booking_folio_transfer_roomcharge: this.folio_transfer
            .id_folio_transfer,
          booking_folio_transfer_minibarcharge: null
        };
        this.updateBookingFolioTransfer({
          id: this.getBookingGuestDetail.id,
          data: data
        });
      } else if (this.folio_transfer.id_folio_transfer_select == 3) {
        data = {
          booking_folio_transfer_roomcharge: null,
          booking_folio_transfer_minibarcharge: this.folio_transfer
            .id_folio_transfer
        };
        this.updateBookingFolioTransfer({
          id: this.getBookingGuestDetail.id,
          data: data
        });
      }
      setTimeout(() => {
        this.fetchGuestBookingDetail({ id: this.getBookingGuestDetail.id });
        this.$modal.hide("foliotransfer-popup");
      }, 2000);
    },
    cancelTransferFolio() {
      this.$dialog
        .confirm("Do you want to cancel Folio Transfer?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          let data = {
            booking_folio_transfer_roomcharge: null,
            booking_folio_transfer_minibarcharge: null
          };
          this.updateBookingFolioTransfer({
            id: this.getBookingGuestDetail.id,
            data: data
          });

          setTimeout(() => {
            this.fetchGuestBookingDetail({ id: this.getBookingGuestDetail.id });
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    }
  },
  mounted() {
    this.fetchProducts();
    this.fetchProductTypes();
    this.fetchClientList();
    this.fetchRooms();
    this.fetchRoomTypeList();
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
.transfer-other-room {
  background-color: yellow;
  color: red !important;
}
.transfer-other-minibar {
  background-color: yellowgreen;
  color: red !important;
}
</style>
