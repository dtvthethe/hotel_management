<template>
  <div id="bill-form">
    <br>
    <h5 class="text-center">
      <strong>HOANG LOC HOTEL</strong>
    </h5>
    <p class="text-center">7-9 Ybil Aleo, Tan Loi, Buon Ma Thuot, DakLak</p>
    <br>
    <h5 class="text-center"><strong>INVOICE</strong></h5>
    <hr>
    <div class="row row-tb-reg">
      <div class="col-md-4"><strong>Folio No.</strong> {{getInvoiceID}}</div>
      <div class="col-md-8"><strong>Client</strong>{{clientName}}</div>
      <div class="col-md-4"><strong>Guest Name</strong>{{getBookingGuestDetail.fullname}}</div>
    </div>
    <hr>
    <div class="row row-tb-reg">
      <table class="tb-booking-infor">
        <tr>
          <th class="col-md-2">Adult</th>
          <th class="col-md-2">Child</th>
          <th class="col-md-6">Room</th>
          <th class="col-md-2">Payment Type</th>
        </tr>
        <tr>
          <td class="td-booking-infor">{{getBookingDetail.adult}}</td>
          <td class="td-booking-infor">{{getBookingDetail.child}}</td>
          <td class="td-booking-infor">{{roomNumber}}</td>
          <td class="td-booking-infor">-</td>
        </tr>
      </table>
    </div>
    <hr>
    <div class="row row-tb-reg">
      <div class="col-md-4"><strong>Date of Arrival</strong>{{this.getBookingDetail.arrive_date | dateFormat('DD/MM/YYYY')}}</div>
      <div class="col-md-4"><strong>Date of Depart</strong>{{this.getBookingDetail.depart_date | dateFormat('DD/MM/YYYY')}}</div>
      <div class="col-md-4"><strong>Night</strong>{{numberNight}}</div>
    </div>
    <div class="row-tb-reg">
      <table class="tb-booking-infor tb-invoice-infor">
        <tr>
          <th>#</th>
          <th>Date</th>
          <th>Room</th>
          <th>Description</th>
          <th>Quantity</th>
          <th>Rate</th>
          <th>Total</th>
        </tr>
        <tr :key="item.id" v-for="(item, index) in invoices">
          <td>{{index+1}}</td>
          <td>{{item.date_order | dateFormat('DD/MM/YYYY')}}</td>
          <td>{{item.room.name}}</td>
          <td>{{item.product.name}}</td>
          <td>{{item.quantity}}</td>
          <td>{{item.price_confirm | currency}}</td>
          <td>{{item.price_confirm * item.quantity | currency}}</td>
        </tr>
        <tr>
          <td colspan="6" class="td-text-align-right">Grand Total</td>
          <td>{{getToTal | currency }}</td>
        </tr>
        <tr>
          <td colspan="6" class="td-text-align-right">Deposit</td>
          <td>{{deposit | currency }}</td>
        </tr>
        <tr>
          <td colspan="6" class="td-text-align-right">Pre-payment</td>
          <td>{{prePayment | currency }}</td>
        </tr>
        <tr>
          <td colspan="6" class="td-text-align-right">Balance</td>
          <td><strong>{{getBalance | currency }}</strong></td>
        </tr>
      </table>
      <div class="row">
        <div class="col-md-4 col-md-offset-8">
          <strong>USD Exchange = {{getBalance | currency }} / {{getExchangeUSD | currency('$')}} = {{getBalance / getExchangeUSD | currency('$')}}</strong>
        </div>
      </div>
    </div>
    <br>
    <div class="row-tb-reg">
      <table class="tb-booking-infor">
        <tr>
          <td>Guest's Signature</td>
          <td>Cashier's Signature</td>
          <td>Reception Manager</td>
        </tr>
      </table>
    </div>

  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "BillReportForm",
  data() {
    return {};
  },
  props:['roomNumber', 'numberNight', 'invoices', 'clientName', 'deposit', 'prePayment'],
  computed: {
    ...mapGetters({
      getBookingDetail: "getBookingDetail",
      getBookingGuestDetail: "getBookingGuestDetail",
      getInvoiceID:"getInvoiceID",
      getExchangeUSD:"getExchangeUSD"
    }),
    getToTal(){
      let total = 0;
      if(this.invoices.length > 0){
        this.invoices.forEach(item=>{
          total += item.quantity * item.price_confirm
        });
      }
      return total;
    },
    getBalance(){
      return this.getToTal - this.deposit - this.prePayment;
    }
  },
  methods: {
    ...mapActions({}),
  },
  mounted: function() {}
};
</script>
<style scoped>
#bill-form {
  font-family: auto;
  font-size: 14px;
}
.text-center {
  text-align: center;
}
.row-tb-reg {
  padding: 0px 50px;
}
.tb-booking-infor{
  width: 100%;
}
.td-booking-infor{
  padding: 0px 25px;
}
.tb-invoice-infor{
  padding: 0px 25px;
  border-collapse: collapse;
  margin: 20px 0px;
}

.tb-invoice-infor, .tb-invoice-infor th, .tb-invoice-infor td {
  border: 1px solid black;
}
.td-text-align-right{
  text-align: right;
  padding-right: 15px;
  font-weight: bold;
}
.text-align-right{
  text-align: right;
}
    
</style>
