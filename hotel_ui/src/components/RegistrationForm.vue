<template>
  <div id="reg-form">
    <br>
    <h5 class="text-center">
      <strong>HOANG LOC HOTEL</strong>
    </h5>
    <p class="text-center">7-9 Ybil Aleo, Tan Loi, Buon Ma Thuot, DakLak</p>
    <br>
    <h5 class="text-center"><strong>REGISTRATION FORM</strong></h5>
    <h5 class="text-center"><strong>PHIẾU ĐĂNG KÝ</strong></h5>
    <hr>
    <div class="row-tb-reg">
      <table class="col-md-8 col-md-offset-2">
        <tr>
          <td>
            Full Name / Họ tên:
            <strong>{{this.getBookingGuestDetail.fullname}}</strong>
          </td>
          <td>
            Room No / Số phòng:
            <strong>{{roomNumber}}</strong>
          </td>
        </tr>
        <tr>
          <td>Email/ Địa Chỉ Email:</td>
          <td>Room Type / Loại Phòng: <strong>{{roomType}}</strong></td>
        </tr>
        <tr>
          <td>Date of Birth / Ngày tháng năm sinh:</td>
          <td>No of Nights/ Số Đêm Lưu Trú: <strong>{{numberNight}}</strong></td>
        </tr>
        <tr>
          <td>Nationality / Quốc Tịch :</td>
          <td>Date of Arrival / Ngày Đến: <strong>{{this.getBookingDetail.arrive_date | dateFormat('DD/MM/YYYY ')}}</strong></td>
        </tr>
        <tr>
          <td>
            Passport No / Số hộ chiếu
            <br>Identify card / Số CMND:
          </td>
          <td>Date of Depature/ Ngày Đi: <strong>{{this.getBookingDetail.depart_date | dateFormat('DD/MM/YYYY')}}</strong></td>
        </tr>
        <tr>
          <td>Method of payment / Phương Thức Thanh Toán :</td>
          <td>Arrival Time / Thời Gian Đến :</td>
        </tr>
        <tr>
          <td class="tab-space-20">
            <input type="checkbox"> In Cash / Tiền Mặt
            <br>
            <input type="checkbox"> Credit Card / Thẻ
            <br>
            <input type="checkbox"> Travel Cheques
          </td>
          <td><div v-if="getIsShowPrice" >Room Rate / Giá Phòng:
            <p class="tab-space-20">
              {{getBookingDetail.price_booking | currency}} x {{numberNight}}(night(s))<br>
              <strong>Σ = {{getBookingDetail.price_booking * numberNight | currency}}</strong>
            </p>
          </div>
          </td>
        </tr>
        <tr>
          <td>Card Type:</td>
          <td>Other guests stay with / Khách cùng lưu trú :</td>
        </tr>
        <tr>
          <td>Card No:</td>
          <td></td>
        </tr>
        <tr>
          <td>Expiry Date :</td>
          <td></td>
        </tr>
      </table>
    </div>
    <hr class="margin-hr-bot">
    <div class="row-tb-reg">
      <table class="tb-regform">
        <tr>
          <td></td>
          <td class="sig-right">
            Guest's Singature
            <br>Chữ Ký Của Khách
          </td>
        </tr>
      </table>
    </div>
    <br>
    <br>
    <br>
    <p class="text-center">
      The hotel will not be held responsible for loss of money or valuables left in rooms
      <br>_Khách sạn sẽ không chịu trách nhiệm về việc mất mát tài sản ở trong phòng khách
      <br>" Please leave your room key at the front desk when you go out
      <br>_Xin vui lòng để lại chìa khóa tại quầy lễ tân khi quý khách ra ngoài
      <br>" Check out time is before 12 noon on the day of depature. A late check out can be arranged subject to availability,
      please contact reception as soon as posible
      <br>_ Giờ trả phòng là trước 12h trưa ngày khách đi. Việc trả phòng muộn tùy thuộc vào khả năng đáp ứng về phòng,
      xin vui lòng liên hệ lễ tân ngay khi cần thiết.
      <br>
      <br>
      <strong>Enjoy your stay with us</strong>
      <br>
      <strong>Chúc quý khách vui vẻ!</strong>


    </p>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "RegistrationForm",
  data() {
    return {};
  },
  props:['roomNumber', 'roomType', 'numberNight'],
  computed: {
    ...mapGetters({
      getBookingDetail: "getBookingDetail",
      getBookingGuestDetail: "getBookingGuestDetail",
      getRoom: "getRoom",
      getIsShowPrice:"getIsShowPrice"
    })
  },
  methods: {
    ...mapActions({}),
    printPage() {
      // var newstr = document.getElementById("reg-form").innerHTML;
      // var oldstr = document.body.innerHTML;
      // document.body.innerHTML = newstr;
      window.print();
      // document.body.innerHTML = oldstr;
      return false;
    }
  },
  mounted: function() {}
};
</script>
<style scoped>
#reg-form {
  font-family: auto;
  font-size: 14px;
}
.text-center {
  text-align: center;
}
.tb-regform {
  width: 100%;
}
.row-tb-reg {
  padding: 0px 50px;
}
.tab-space-20 {
  padding-left: 20px;
}
.tool {
  background-color: #624373;
  color: #ffffff;
}
.tool .close-btn {
  float: right;
  margin-right: 48px;
  color: #fff;
}
.tool label {
  font-weight: normal;
  font-size: small;
}
.margin-hr-bot {
  margin-top: 10px;
  margin-bottom: 0px;
  clear: both;
}
.sig-right {
  text-align: right;
  padding-right: 100px;
}
</style>
