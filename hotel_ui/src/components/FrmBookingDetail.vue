<template>
  <form role="form" id="frmbookingdetail" class="modal-open">
    <!-- Nav tabs{{getRooms(1)}} -->
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
        <a class="btn btn-sm btn-default" @click="show('minibar-popup', 'new')" v-show="showButtontoClick">Add new</a>
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
            <tr :key="item.id" v-for="item in getInvoiceMinibar">
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
      </div>
      <!-- //extracharge -->
      <!-- foliodetail -->
      <div role="tabpanel" class="tab-pane" id="foliodetail">
        <div class="row">
          <fieldset class="col-md-2">
            <legend class>Payment</legend>
            <div>
              <p>Folio NO: {{getInvoiceID}}</p>
              <p>Balance: {{balanceTotal | currency}}</p>
              <p>{{strFolioTranfer}}</p>
            </div>
          </fieldset>
          <fieldset class="col-md-10">
            <legend class>Payment</legend>
            <div>
              <a
                class="btn btn-sm btn-default"
                @click="showPaymentPopup('payment-popup', 'new')"
                v-show="showPaymentButtontoClick"
              >Add Payment</a>
            </div>
            <div class="col-md-12">
              <table class="table table-fixed table-payment">
                <thead>
                  <tr>
                    <th class="col-md-2">Date</th>
                    <th class="col-md-2">Credit</th>
                    <th class="col-md-2">Payment</th>
                    <th class="col-md-1">Deposit</th>
                    <th class="col-md-3">Desciption</th>
                    <th class="col-md-2">Option</th>
                  </tr>
                </thead>
                <tbody>
                  <tr :key="item.id" v-for="item in getBookingPayments">
                    <td class="col-md-2">{{item.date_pay | dateFormat('DD/MM/YYYY HH:mm:ss')}}</td>
                    <td class="col-md-2">{{item.credit | currency}}</td>
                    <td class="col-md-2">{{item.payment_type.name}}</td>
                    <td class="col-md-1">{{item.deposit == true ? 'Yes':'_'}}</td>
                    <td class="col-md-3">{{item.desciption}}</td>
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
            <a class="btn btn-sm btn-warning" @click="addRoomCharge()" v-show="showButtontoClick">Add Room Charge</a>
            <a
              class="btn btn-sm btn-default"
              :class="{'disabled' : disableButtonByFolioTranferBooking}"
              v-show="showButtontoClick"
              @click="transferFolio()"
            >Folio Transfer</a>
            <a
              class="btn btn-sm btn-danger"
              :class="{'disabled' : disableButtonByFolioTranferBooking2}"
              v-show="showButtontoClick"
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
                <tr :key="item.id" v-for="item in getInvoiceAllCharge">
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >{{item.date_order | dateFormat('DD/MM/YYYY HH:mm:ss')}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >{{item.room.name}}</td>
                  <td
                    class="col-md-3"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >
                    {{item.product.name}}
                    <span
                      v-if="item.product.id == 1"
                    >({{item.date_session | dateFormat('DD/MM/YYYY')}})</span>
                  </td>
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >{{item.price_confirm | currency}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >{{item.quantity}}</td>
                  <td
                    class="col-md-2"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >{{item.total | currency}}</td>
                  <td
                    class="col-md-1"
                    :class="{'transfer-other-room':(item.invoice != getInvoiceID && item.product.id == 1), 'transfer-other-minibar':(item.invoice != getInvoiceID && item.product.id != 1), 'room-charge':(item.invoice == getInvoiceID && item.product.id == 1)}"
                  >
                    <span
                      v-if="item.invoice == getInvoiceID && item.product.id == 1"
                      style="display: inline"
                    >
                      <a
                        style="cursor: pointer;"
                        @click="show('roomcharge-popup', 'edit', item.id)"
                      >Edit</a> |
                      <a
                        style="cursor: pointer;"
                        @click="deleteRoomChargeClick(item.id)"
                      >Delete</a>
                    </span>
                    <span v-else>&emsp;</span>
                  </td>
                </tr>
              </tbody>
            </table>
            <p>Total = {{getTotalAllCharge | currency}}</p>
          </fieldset>
        </div>
      </div>
      <!-- foliodetail -->
    </div>
    <input
      type="button"
      class="btn btn-default margin-bottom-button"
      data-dismiss="modal"
      value="Save"
      @click="saveReveration"
    >
    <input
      type="button"
      class="btn btn-success margin-bottom-button"
      value="Check-in"
      data-dismiss="modal"
      @click="onButtonBottomClick('checkin')"
    >

    <input
      type="button"
      class="btn btn-warning margin-bottom-button"
      value="Check-out"
      data-dismiss="modal"
      @click="onButtonBottomClick('checkout')"
    >
    <input
      type="button"
      class="btn btn-danger margin-bottom-button"
      value="Cancel Booking"
      data-dismiss="modal"
      @click="onButtonBottomClick('delete')"
    >

    <input
      type="button"
      class="btn btn-default margin-bottom-button"
      value="No-Show"
      @click="onButtonNoShowClick()"
    >
    <div class="tool-export">
      <a href="javascript:void(0);" @click="onclickReg()"><i class="fa fa-square-o"></i>Reg Form</a>
      <a href="javascript:void(0);" @click="onclickBill('bill')"><i class="fa fa-plus-square"></i>Bill</a>
      <a href="javascript:void(0);" @click="onclickBill('room')"><i class="fa fa-check-square-o"></i>Bill Room</a>
      <a href="javascript:void(0);" @click="onclickBill('extra')"><i class="fa  fa-plus-square-o"></i>Bill Extra Charge</a>
    </div>
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
      <br>Deposit:
      <input type="checkbox" v-model="bookingpayment.deposit">
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

    <!-- popup roomcharge -->
    <popup-modal name="roomcharge-popup" :clickToClose="false">
      Room rate:
      <input type="number" v-model="roomcharge.price_confirm">
      <i>{{roomcharge.price_confirm | currency}}</i>
      <br>

      <input type="button" value="Save" @click="onSaveRoomChargeClick()">
      <input type="button" value="Close" @click="hide('roomcharge-popup')">
    </popup-modal>
    <!--// popup roomcharge -->

    <!-- popup foliotransfer -->
    <popup-modal name="foliotransfer-popup" :clickToClose="false">
      Folio ID:
      <input type="text" v-model="folio_transfer.id_folio_transfer">
      <i>{{messageErrorFolioTransfer}}</i>
      <i>{{getErrorTransfer}}</i>
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

    <!-- popup no-show -->
    <popup-modal name="noshow-popup" :clickToClose="false">
      <input type="checkbox" v-model="post_charge.isShowPrice" >
      <input type="text" v-model="post_charge.price_noshow" :disabled="!post_charge.isShowPrice"> <i>{{post_charge.price_noshow | currency}}</i><br>

      <input type="button" value="Post" @click="postNoShow('post')">
      <input type="button" value="Post and Charge" @click="postNoShow('post-charge')">
      <input type="button" value="Close" @click="hide('noshow-popup')">
    </popup-modal>
    <!--// popup no-show -->
    <!-- popup reg form -->
    <popup-modal name="reg-form" width="100%" height="1000px" :clickToClose="false">
      <div class="tool">
        <input type="checkbox" id="show-rate-room" v-model="is_showPrice">
        <label for="show-rate-room">Show rate room</label>
        <a class="close-btn" href="javascript:void(0);" @click="hide('reg-form')">Close</a>
      </div>
      <RegistrationForm :room-number="roomName.room" :room-type="roomName.room_type" :number-night="durationTwoDate"></RegistrationForm>
    </popup-modal>
    <!--// popup reg form -->

    <!-- popup bill form -->
    <popup-modal name="bill-form" width="100%" height="1500px" :clickToClose="false">
      <div class="tool">
        <label> </label>
        <a class="close-btn" href="javascript:void(0);" @click="hide('bill-form')">Close</a>
      </div>
      <BillReportForm :pre-payment="getPrePayment" :deposit="getDeposit" :number-night="durationTwoDate" :room-number="roomName.room" :invoices="invoice_bill" :client-name="roomName.client" ></BillReportForm>
    </popup-modal>
    <!--// popup bill form -->
  </form>
</template>
<script>
import Datepicker from "vuejs-datepicker"
import { mapGetters, mapActions } from "vuex"
import { differenceInDays, addDays, format, isSameDay, parse } from "date-fns"
import RegistrationForm from "./RegistrationForm"
import BillReportForm from "./BillReportForm"


export default {
  name: "FrmBookingDetail",
  components: {
    Datepicker,
    RegistrationForm,
    BillReportForm
  },
  data: function() {
    return {
      invoice_bill:[],
      roomName:{
        room:null,
        room_type:null,
        client: null,
      },
      disabledDatesArrive: {
        from: null
      },
      disabledDatesDepart: {
        to: null
      },
      post_charge:{
        price_noshow:0,
        isShowPrice:false
      },
      durationTwoDate: -1,
      roomtype_id: -1,
      product_type_id: -1,
      second_popup_status: "",
      minibarcharge: {
        price_confirm: 0,
        quantity: 1,
        product: 0,
      },
      bookingpayment: {
        credit: 0,
        desciption: null,
        booking: -1,
        payment_type: -1,
        deposit:false,
      },
      roomcharge: {
        price_confirm: 0,
        quantity: 1,
        product: 0,
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
      getMinibarChargeById: "getMinibarChargeById",
      getBookingPayments: "getBookingPayments",
      getBookingPaymentById: "getBookingPaymentById",
      getRoomCharges: "getRoomCharges",
      getRoomChargeById: "getRoomChargeById",
      getPaymentTypes: "getPaymentTypes",
      getSessionDate: "getSessionDate",
      getInvoiceID: "getInvoiceID",
      getInvoices: "getInvoices",
      getErrorTransfer: "getErrorTransfer",
      getIsShowPrice:"getIsShowPrice"
    }),
    getDeposit(){
      let total = 0;
      this.getBookingPayments.forEach(item => {
        if(item.deposit == true){
          total += item.credit;
        }
      });
      return total;
    },
    getPrePayment(){
      let total = 0;
      this.getBookingPayments.forEach(item => {
        if(item.deposit == false){
          total += item.credit;
        }
      });
      return total;
    },
    getInvoiceMinibar() {
      if (this.getInvoices.length > 0) {
        let invs = this.getInvoices
          .find(item => item.id == this.getInvoiceID)
          .invoices.filter(item => item.product.id != 1);
        let invs_formats = invs.map(item => {
          return {
            ...item,
            date_order: parse(item.date_order)
          };
        });
        return invs_formats;
      } else {
        return [];
      }
    },
    getInvoiceAllCharge() {
      if (this.getInvoices.length > 0) {
        let lst = [];
        this.getInvoices.forEach(invoice => {
          invoice.invoices.forEach(item => {
            if(item.isShow == true){
              lst.push({
                ...item,
                room: invoice.booking.room,
                date_order: parse(item.date_order),
                date_session: parse(item.date_session),
                total: item.quantity * item.price_confirm
              });
            }
          });
        });
        return lst;
      } else {
        return [];
      }
    },
    getTotalAllCharge() {
      if (this.getInvoices.length > 0) {
        let total = 0;
        this.getInvoices.forEach(invoice => {
          invoice.invoices.forEach(item => {
            total += item.quantity * item.price_confirm;
          });
        });
        return total;
      } else {
        return 0;
      }
    },
    booking_code: {
      get() {
        if(this.getFrmType.booking_code != undefined){
          return this.getFrmType.booking_code
        }
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
    is_showPrice: {
      get() {
        return this.getIsShowPrice
      },
      set() {
        this.switchShowPrice();
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
    disableButtonByFolioTranferBooking() {
      if (this.getInvoiceID == null) {
        return true;
      }
      if (this.getInvoices.length == 0 || this.getInvoices.length > 1) {
        return true;
      }
      let invoice = this.getInvoices.find(item => this.getInvoiceID == item.id);
      if (
        invoice.folio_transfer_minibarcharge == null &&
        invoice.folio_transfer_roomcharge == null
      ) {
        return false;
      } else {
        return true;
      }
    },
    disableButtonByFolioTranferBooking2() {
      if (this.getInvoiceID == null) {
        return true;
      }
      if (this.getInvoices.length == 0 || this.getInvoices.length > 1) {
        return true;
      }
      let invoice = this.getInvoices.find(item => this.getInvoiceID == item.id);
      if (
        invoice.folio_transfer_minibarcharge == null &&
        invoice.folio_transfer_roomcharge == null
      ) {
        return true;
      } else {
        return false;
      }
    },
    messageErrorFolioTransfer() {
      if (this.folio_transfer.id_folio_transfer == this.getInvoiceID) {
        return "Can't set to this Folio ID.";
      }
      return null;
    },
    balanceTotal() {
      if (this.getBookingGuestDetail.id == undefined) {
        return 0;
      }
      let totalPayment = 0;
      this.getBookingPayments.forEach(item => {
        totalPayment += item.credit;
      });

      if (this.getInvoiceID == null) {
        return totalPayment * -1;
      }
      if (this.getInvoices.length <= 0) {
        return totalPayment * -1;
      }

      
      let invoice = this.getInvoices.find(item => this.getInvoiceID == item.id);
      if (
        invoice.folio_transfer_minibarcharge != null &&
        invoice.folio_transfer_roomcharge != null
      ) {
        return totalPayment * -1;
      }
      if (
        invoice.folio_transfer_minibarcharge != null &&
        invoice.folio_transfer_roomcharge == null
      ) {
        let total = 0;
        this.getInvoices.forEach(invoice => {
          invoice.invoices.forEach(item => {
            if (item.product.id == 1) {
              total += item.quantity * item.price_confirm;
            }
          });
        });
        return total - totalPayment;
      }
      if (
        invoice.folio_transfer_minibarcharge == null &&
        invoice.folio_transfer_roomcharge != null
      ) {
        let total = 0;
        this.getInvoices.forEach(invoice => {
          invoice.invoices.forEach(item => {
            if (item.product.id != 1) {
              total += item.quantity * item.price_confirm;
            }
          });
        });
        return total - totalPayment;
      }

      return this.getTotalAllCharge - totalPayment;
    },
    strFolioTranfer() {
      if (this.getBookingGuestDetail.id == undefined) {
        return "";
      }
      if (this.getInvoiceID == null) {
        return "";
      }
      if (this.getInvoices.length <= 0) {
        return "";
      }
      let iDFolio = 0;
      let strFolio = "";
      let invoice = this.getInvoices.find(item => this.getInvoiceID == item.id);
      if (
        invoice.folio_transfer_minibarcharge == null &&
        invoice.folio_transfer_roomcharge == null
      ) {
        return "";
      } else {
        if (invoice.folio_transfer_roomcharge != null) {
          // room charge
          iDFolio = invoice.folio_transfer_roomcharge;
          strFolio += "Room Charge";
        }

        if (invoice.folio_transfer_minibarcharge != null) {
          // minibar
          iDFolio = invoice.folio_transfer_minibarcharge;
          if (strFolio == "") {
            strFolio += "Minibar Charge";
          } else {
            strFolio += ", Minibar Charge";
          }
        }

        return "Folio ID:" + iDFolio + "(" + strFolio + ")";
      }
    },
    showButtontoClick(){
      return this.getBookingDetail.booking_status == 2;
    },
    showPaymentButtontoClick(){
      return this.getBookingDetail.booking_status == 2 || this.getBookingDetail.booking_status == 1;
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
      removeBookings:"removeBookings",
      deleteReveration:"deleteReveration",
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
      fetchBookingPayments: "fetchBookingPayments",
      postBookingPayment: "postBookingPayment",
      putBookingPayment: "putBookingPayment",
      deleteBookingPayment: "deleteBookingPayment",
      deleteRoomCharge: "deleteRoomCharge",
      updateBookingFolioTransfer: "updateBookingFolioTransfer",
      postInvoiceDetail: "postInvoiceDetail",
      updateInvoiceDetail: "updateInvoiceDetail",
      updateInvoiceDetailPriceConfirm: "updateInvoiceDetailPriceConfirm",
      deleteInvoiceDetail: "deleteInvoiceDetail",
      fetchInvoices: "fetchInvoices",
      fetchGuestLeger:"fetchGuestLeger",
      updateBookingCheckIn:"updateBookingCheckIn",
      updateBookingCheckOut:"updateBookingCheckOut",
      removeCalendarBooking:"removeCalendarBooking",
      removeGuestLeger:"removeGuestLeger",
      updateBookingStatusNoShow:"updateBookingStatusNoShow",
      updateBookingStatusNoShowPostCharge:"updateBookingStatusNoShowPostCharge",
      updateBookingStatusCancel:"updateBookingStatusCancel",
      switchShowPrice:"switchShowPrice",
    }),
    onclickBill(name){
      this.roomName.room = this.getRooms(-1).find(item => item.id == this.room).name;
      this.roomName.client = this.getClients.find(item => item.id == this.client).name;
      if(name == 'bill'){
        this.invoice_bill = this.getInvoiceAllCharge;
      }
      else if(name == 'room'){
        this.invoice_bill = this.getInvoiceAllCharge.filter(item => item.product.id == 1)
      }
      else if(name == 'extra'){
        this.invoice_bill = this.getInvoiceAllCharge.filter(item => item.product.id != 1)
      }
      else{
        return;
      }
      this.$modal.show('bill-form');
    },
    onclickReg(){

      this.roomName.room = this.getRooms(-1).find(item => item.id == this.room).name;
      this.roomName.room_type = this.getRoomTypes.find(item => item.id == this.roomtype_id).name;
      this.$modal.show('reg-form');
    },
    onButtonNoShowClick(){
      this.$modal.show('noshow-popup');
    },
    postNoShow(type_post){
      if(type_post == 'post'){
        this.updateBookingStatusNoShow({booking_id: this.getBookingGuestDetail.id})
      }
      else if(type_post == 'post-charge'){
        this.updateBookingStatusNoShowPostCharge({booking_id: this.getBookingGuestDetail.id, date_session: this.getSessionDate, price_confirm: this.post_charge.price_noshow})
      }
      else{
        return;
      }
      setTimeout(() => {
        if(this.getFrmType.type == 'fo'){
          this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
        }
        else if(this.getFrmType.type == 'ca'){
          this.fetchGuestBookings({
            arrive_date: this.getFrmType.date_start,
            depart_date: this.getFrmType.date_stop
          });
        }
        else if(this.getFrmType.type == 'leger'){
          this.fetchGuestLeger({
            ...this.getFrmType.data.filter_field,
            arrive_date: format(this.getFrmType.data.filter_field.arrive_date, "YYYY-MM-DD"),
            depart_date: format(this.getFrmType.data.filter_field.depart_date, "YYYY-MM-DD")
          });
        }
        else{
          return;
        }
        this.$modal.hide('noshow-popup');
      }, 2000);
    },
    onButtonBottomClick(str_type){
      let data_booking = {
        id: this.getBookingDetail.id,
        action_name: str_type
      };

      if(str_type == 'delete'){
        this.$dialog
          .confirm("Do you want to cancel this reservation?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateBookingStatusCancel({booking_id: this.getBookingGuestDetail.id});
            setTimeout(() => {
              if(this.getFrmType.type == 'fo'){
                this.removeBookings(data_booking.id);
              }
              else if(this.getFrmType.type == 'ca'){
                this.removeCalendarBooking(data_booking.id);
              }
              else if(this.getFrmType.type == 'leger'){
                this.fetchGuestLeger({
                  ...this.getFrmType.data.filter_field,
                  arrive_date: format(this.getFrmType.data.filter_field.arrive_date, "YYYY-MM-DD"),
                  depart_date: format(this.getFrmType.data.filter_field.depart_date, "YYYY-MM-DD")
                });
              }
              else{
                return;
              }
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else if(str_type == 'checkin'){
        this.$dialog
          .confirm("Do you want to check-in this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            let guest_id = this.getFrmType.guest_id;
            this.updateBookingCheckIn({booking_id: data_booking.id, guest_id});
            setTimeout(() => {
              if(this.getFrmType.type == 'fo'){
                this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              }
              else if(this.getFrmType.type == 'ca'){
                this.fetchGuestBookings({
                  arrive_date: this.getFrmType.date_start,
                  depart_date: this.getFrmType.date_stop
                });
              }
              else if(this.getFrmType.type == 'leger'){
                this.fetchGuestLeger({
                  ...this.getFrmType.data.filter_field,
                  arrive_date: format(this.getFrmType.data.filter_field.arrive_date, "YYYY-MM-DD"),
                  depart_date: format(this.getFrmType.data.filter_field.depart_date, "YYYY-MM-DD")
                });
              }
              else{
                return;
              }

              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else if(str_type == 'checkout'){
        this.$dialog
          .confirm("Do you want to check-out this room?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.updateBookingCheckOut(data_booking.id);
            setTimeout(() => {
              // this.fetchRoomWithTypes();
              // this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              if(this.getFrmType.type == 'fo'){
                this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
              }
              else if(this.getFrmType.type == 'ca'){
                this.fetchGuestBookings({
                  arrive_date: this.getFrmType.date_start,
                  depart_date: this.getFrmType.date_stop
                });
              }
              else if(this.getFrmType.type == 'leger'){
                this.fetchGuestLeger({
                  ...this.getFrmType.data.filter_field,
                  arrive_date: format(this.getFrmType.data.filter_field.arrive_date, "YYYY-MM-DD"),
                  depart_date: format(this.getFrmType.data.filter_field.depart_date, "YYYY-MM-DD")
                });
              }
              else{
                return;
              }
              dialog.close();
            }, 2000);
          })
          .catch(() => {
            // on cancel click
          });
      }
      else{
        return;
      }
    },
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
              this.fetchBookings(this.getFrmType.data_value);
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
          if (this.getFrmType.type == "leger") {
            setTimeout(() => {
              this.fetchGuestLeger({
                ...this.getFrmType.data.filter_field,
                arrive_date: format(this.getFrmType.data.filter_field.arrive_date, "YYYY-MM-DD"),
                depart_date: format(this.getFrmType.data.filter_field.depart_date, "YYYY-MM-DD")
              });
            }, 2000);
          }
        }
      } else {
        this.postReveration();
        if (this.getFrmType.method == "new") {
          if (this.getFrmType.type == "fo") {
            setTimeout(() => {
              this.fetchBookings(this.getFrmType.data_value);
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
          invoice: this.getInvoiceID,
          date_session: format(this.getSessionDate, "YYYY-MM-DD")
        };
        this.postInvoiceDetail(data);
        setTimeout(() => {
          this.fetchInvoices({ invoice_id: this.getInvoiceID });
          this.$modal.hide("minibar-popup");
          this.minibarcharge = {
            price_confirm: 0,
            quantity: 1,
            product: 0,
          }
        }, 2000);
      }
      if (this.second_popup_status == "edit") {
        this.updateInvoiceDetail({
          data: this.minibarcharge,
          id: this.id_editing
        });
        setTimeout(() => {
          this.fetchInvoices({ invoice_id: this.getInvoiceID });
          this.$modal.hide("minibar-popup");
          this.minibarcharge = {
            price_confirm: 0,
            quantity: 1,
            product: 0,
          }
        }, 2000);
      }
    },
    show(popup_name, status, id = 0) {
      if (id > 0) {
        if (popup_name == "minibar-popup") {
          let minidt = this.getInvoiceMinibar.find(item => item.id == id);
          this.id_editing = id;
          this.minibarcharge = {
            price_confirm: minidt.price_confirm,
            quantity: minidt.quantity,
            product: minidt.product.id,
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
            payment_type: bkpayment.payment_type.id,
            deposit: false,
          };
        }
        if (popup_name == "roomcharge-popup") {
          let roomcharge = this.getInvoiceAllCharge.find(item => item.id == id);
          if(roomcharge.product.id == 1){
              this.id_editing = id;
              this.roomcharge = {
                price_confirm: roomcharge.price_confirm,
                quantity: 1,
                product: 1,
              };
          }
         
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
          this.deleteInvoiceDetail(id);

          setTimeout(() => {
            this.fetchInvoices({ invoice_id: this.getInvoiceID });
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
          this.deleteInvoiceDetail(id);

          setTimeout(() => {
            this.fetchInvoices({ invoice_id: this.getInvoiceID });
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
          this.bookingpayment = {
            credit: 0,
            desciption: null,
            booking: -1,
            payment_type: -1,
            deposit: false
          }
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
          this.bookingpayment = {
            credit: 0,
            desciption: null,
            booking: -1,
            payment_type: -1,
            deposit: false
          }
        }, 2000);
      }
    },
    onSaveRoomChargeClick() {
      if (this.second_popup_status == "edit") {
        this.updateInvoiceDetail({
          data: this.roomcharge,
          id: this.id_editing
        });
        setTimeout(() => {
          this.fetchInvoices({ invoice_id: this.getInvoiceID });
          this.$modal.hide("roomcharge-popup");
        }, 2000);
      }
    },
    addRoomCharge() {
      let data = {
        booking: this.getBookingGuestDetail.id,
        price_confirm: this.price,
        date_session: format(this.getSessionDate, "YYYY-MM-DD"),
        quantity: 1,
        invoice: this.getInvoiceID,
        product: 1
      };
      if (this.getInvoiceAllCharge.filter(
          item =>
            (isSameDay(parse(this.getSessionDate), parse(item.date_session)) &&
            item.product.id == 1) && (item.invoice == this.getInvoiceID)
        ).length == 0
      ) {
        this.$dialog
          .confirm("Do you want to add room charge?", {
            loader: true,
            okText: "Yes",
            cancelText: "No"
          })
          .then(dialog => {
            // on OK click
            this.postInvoiceDetail(data);

            setTimeout(() => {
              // this.fetchRoomCharges(this.getBookingGuestDetail.id);
              this.fetchInvoices({ invoice_id: this.getInvoiceID });
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
          folio_transfer_roomcharge: this.folio_transfer.id_folio_transfer,
          folio_transfer_minibarcharge: this.folio_transfer.id_folio_transfer
        };
        this.updateBookingFolioTransfer({
          id: this.getInvoiceID,
          data: data
        });
      } else if (this.folio_transfer.id_folio_transfer_select == 2) {
        data = {
          folio_transfer_roomcharge: this.folio_transfer.id_folio_transfer,
          folio_transfer_minibarcharge: null
        };
        this.updateBookingFolioTransfer({
          id: this.getInvoiceID,
          data: data
        });
      } else if (this.folio_transfer.id_folio_transfer_select == 3) {
        data = {
          folio_transfer_roomcharge: null,
          folio_transfer_minibarcharge: this.folio_transfer.id_folio_transfer
        };
        this.updateBookingFolioTransfer({
          id: this.getInvoiceID,
          data: data
        });
      }
      setTimeout(() => {
        if (this.getErrorTransfer == null) {
          this.fetchInvoices({ invoice_id: this.getInvoiceID });
          this.$modal.hide("foliotransfer-popup");
        }
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
            folio_transfer_roomcharge: null,
            folio_transfer_minibarcharge: null
          };
          this.updateBookingFolioTransfer({
            id: this.getInvoiceID,
            data: data
          });

          setTimeout(() => {
            this.fetchInvoices({ invoice_id: this.getInvoiceID });
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
.room-charge {
  background-color: yellow;
}
.transfer-other-room {
  background-color: yellow;
  color: red !important;
}
.transfer-other-minibar {
  background-color: yellowgreen;
  color: red !important;
}
.tool{
  background-color: #624373;
  color:#fff;
}
.tool input{}
.tool .show-rate-room{
  
}
.tool .close-btn{
  color: white;
  font-family: auto;
  float: right;
  margin-right: 50px;
  font-size: smaller;
  font-weight: normal;
}

</style>
