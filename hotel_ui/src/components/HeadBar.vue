<template>
  <div id="head-bar">
    <!--header start-->
    <header class="header fixed-top clearfix">
      <!--logo start-->
      <div class="brand">
        <a href="/" class="logo">Hoàng Lộc Hotel</a>
        <div class="sidebar-toggle-box">
          <div class="fa fa-bars" @click="switchMenu()"></div>
        </div>
      </div>
      <!--logo end-->
     
      <div class="top-nav clearfix">
        <!--search & user info start-->
        <ul class="nav pull-right top-menu">
          <!-- user login dropdown start-->
          <li class="dropdown">
            <a data-toggle="dropdown" class="dropdown-toggle" href="#">
              <img
                v-if="this.user_infor.avatar == undefined || this.user_infor.avatar == 'null'"
                src="../assets/images/no-avatar.png"
              >
              <img v-else :src="this.user_infor.avatar">
              <span class="username">{{this.user_infor.fullname}}</span>

              <b class="caret"></b>
            </a>
            <ul class="dropdown-menu extended logout">
              <li>
                <a href="javascript:void(0);" @click="show('new-user-popup')">
                  <i class="fa fa-suitcase"></i>Profile
                </a>
              </li>
              <li>
                <a href="javascript:void(0);" @click="show('password-user-popup')">
                  <i class="fa fa-qrcode"></i>Change Password
                </a>
              </li>
              <li>
                <a href="javascript:void(0);" @click="onLogOutClick">
                  <i class="fa fa-key"></i> Log Out
                </a>
              </li>
              <li>
                Working on: <i>{{getSessionDate}}</i>
              </li>
            </ul>
          </li>
          <!-- user login dropdown end -->
        </ul>
        <!--search & user info end-->
      </div>
    </header>
    <!--header end-->
    <!--sidebar start-->
    <aside>
      <div id="sidebar" class="nav-collapse" ref="sidebar">
        <!-- sidebar menu start-->
        <div class="leftside-navigation">
          <ul class="sidebar-menu" id="nav-accordion">
            <li>
              <router-link to="/">
                <i class="fa fa-first-order"></i>
                <span>Front Desk</span>
              </router-link>
            </li>
            <li>
              <router-link to="/calendar">
                <i class="fa fa-calendar"></i>
                <span>Calendar Booking</span>
              </router-link>
            </li>
            <li>
              <router-link to="/nightaudit">
                <i class="fa fa-key"></i>
                <span>Night Audit</span>
              </router-link>
            </li>
            <li>
              <router-link to="/guestleger">
                <i class="fa fa-info"></i>
                <span>Guest Leger</span>
              </router-link>
            </li>
            <li>
              <router-link to="/roomstatus">
                <i class="fa fa-calendar"></i>
                <span>Room Status</span>
              </router-link>
            </li>
            <li class="sub-menu">
              <a href="javascript:;">
                <i class="fa fa-book"></i>
                <span>Report</span>
              </a>
              <ul class="sub">
                <li>
                  <router-link to="/checkin">
                    <i class="fa fa-sign-in"></i>
                    <span>Pending Check-in</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/checkout">
                    <i class="fa fa-plane"></i>
                    <span>Pending Check-out</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/inhouse">
                    <i class="fa fa-refresh"></i>
                    <span>In-House List</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/breakfast">
                    <i class="fa fa-glass"></i>
                    <span>Breakfast List</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/houseskeeping">
                    <i class="fa fa-anchor"></i>
                    <span>HouseSkeeping</span>
                  </router-link>
                </li>
                <!-- <li>
                  <a href="#">Daily Payment</a>
                </li>
                <li>
                  <a href="#">Extra Charge</a>
                </li> -->
              </ul>
            </li>
            <!-- <li class="sub-menu">
              <a href="javascript:;">
                <i class="fa fa-puzzle-piece"></i>
                <span>Minibar/Services</span>
              </a>
              <ul class="sub">
                <li>
                  <router-link to="/producttype">
                    <i class="fa fa-align-right"></i>
                    <span>Product Types</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/product">
                    <i class="fa fa-leaf"></i>
                    <span>Products</span>
                  </router-link>
                </li>
              </ul>
            </li> -->
            <!-- <li class="sub-menu">
              <a href="javascript:;">
                <i class="fa fa-braille"></i>
                <span>Rooms</span>
              </a>
              <ul class="sub">
                <li>
                  <router-link to="/roomtype">
                    <i class="fa fa-align-left"></i>
                    <span>Room Types</span>
                  </router-link>
                </li>
                <li>
                  <router-link to="/room">
                    <i class="fa fa-home"></i>
                    <span>Rooms</span>
                  </router-link>
                </li>
              </ul>
            </li> -->
            <!-- <li class="sub-menu">
              <router-link to="/user">
                <i class="fa fa-user"></i>
                <span>User Management</span>
              </router-link>
            </li> -->
          </ul>
        </div>
        <!-- sidebar menu end-->
      </div>
    </aside>
    <!--sidebar end-->

    <!-- Modal -->
    <popup-modal name="new-user-popup" :clickToClose="false" :height="350">
      <!-- password:
      <input type="password" v-model="user.password">-->
      <form>
        <h3>Your Profile</h3>
        <div class="form-group">
          <label for="username">Username</label>
          <input class="form-control m-bot15" :disabled="true" type="input" id="username" v-model="user.username">
        </div>
        <div class="form-group">
          <label for="first_name">First Name</label>
          <input class="form-control m-bot15" type="input" v-model="user.first_name" id="first_name">
        </div>
        <div class="form-group">
          <label for="last_name">Last Name</label>
          <input class="form-control m-bot15" type="input" v-model="user.last_name" id="last_name">
        </div>
        <div class="form-group">
          <label for="user_email">Email Address</label>
          <input class="form-control m-bot15" type="email" id="user_email" v-model="user.email">
        </div>
        <!-- <div class="form-group">
          <label for="avatar">Avatar</label>
          <input type="file" @change="onImageChange" id="avatar" class="form-control">
        </div> -->

        <input type="button" class="btn btn-success" value="Save" @click="onSaveUserClick()">
        <input type="button" class="btn btn-default" value="Close" @click="hide('new-user-popup')">
      </form>
    </popup-modal>

    <popup-modal name="password-user-popup" :clickToClose="false" :height="350">
      <form>
        <h3>Change Password</h3>
        <div class="form-group">
          <label for="txtpw">Old Password <i class="text-danger">{{user_pw.error_empty}}</i></label>
          <input class="form-control m-bot15" type="password" id="txtpw" name="txtpw" v-model="user_pw.pw">
        </div>
        <div class="form-group">
          <label for="txtpw2">New Password <i class="text-danger">{{user_pw.error}}</i><i class="text-danger">{{user_pw.error_empty}}</i></label>
          <input class="form-control m-bot15" type="password" id="txtpw2" name="txtpw2" v-model="user_pw.password">
        </div>
        <div class="form-group">
          <label for="txtpw3">Confirm Password <i class="text-danger">{{user_pw.error_empty}}</i></label>
          <input class="form-control m-bot15" type="password" id="txtpw3" name="txtpw3" v-model="user_pw.password2">
        </div>
        <input type="button" class="btn btn-success" value="Save" @click="onSavePasswordClick()">
        <input type="button" class="btn btn-default" value="Close" @click="hide('password-user-popup')">
      </form>
    </popup-modal>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import { format, parse } from "date-fns";
import { DATA_NAME_FULLNAME, DATA_NAME_AVATAR } from "../store/config";

export default {
  name: "HeadBar",
  data() {
    return {
      notify_list:{},
      user_infor: {
        avatar: null,
        fullname: null
      },
      user: {
        id: 0,
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        // avatar: null
      },
      user_pw:{
        pw:null,
        password:null,
        password2:null,
        error:null,
        error_empty:null
      }
    };
  },
  computed: {
    ...mapGetters({
      getUserByUsername: "getUserByUsername",
      getUserEditor: "getUserEditor",
      getSessionDate: "getSessionDate",
      getBookings: "getBookings",
      getRooms: "getRooms"
    }),
    getBookingFormat(){
      if(this.getBookings.length == 0){
        return [];
      }
      let bookings = []

      this.getBookings.forEach(item =>{
        item.booking.arrive_date = parse(item.booking.arrive_date);
        item.booking.depart_date = parse(item.booking.depart_date);
        bookings.push({
          ...item,
          room_name: this.getRooms(-1).find(
              room => room.id == item.booking.room
            ).name
        });
      });
      return bookings;
    },
    
    
  },
  methods: {
    ...mapActions({
      switchMenu: "switchMenu",
      setWidthMenu: "setWidthMenu",
      removeTokenLocal: "removeTokenLocal",
      putPerson: "putPerson",
      fetchUserByUsername: "fetchUserByUsername",
      fetchUserbyID: "fetchUserbyID",
      putPersonUpdate: "putPersonUpdate",
      fetchSessionDate: "fetchSessionDate",
      fetchBookings: "fetchBookings",
      fetchRooms: "fetchRooms",
      putUserPassword:"putUserPassword"
    }),
    notifyList() {
      // if(this.getBookingFormat.length == 0){
      //   return [];
      // }
      // this.getBookingFormat.forEach(item => {
      //   if(item.booking.booking_status.id == 2 && isSameDay(parse(item.booking.depart_date),parse(this.getSessionDate))){
      //     checkout_list.push(item);
      //   }
      //   else if(item.booking.booking_status.id == 1){
      //     checkin_list.push(item);
      //   }
      //   else {
      //     inhouse_list.push(item);
      //   }
      // });
      // this.notify_list = {
      //   checkin: checkin_list,
      //   checkout: checkout_list,
      //   inhouse: inhouse_list
      // };
      return [];
    },
    onLogOutClick() {
      this.removeTokenLocal();
    },
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    onImageChange(e) {
      let files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      let a = URL.createObjectURL(e.target.files[0]);
      URL.revokeObjectURL(a);
      this.createImage(files[0]);
    },
    createImage(file) {
      let reader = new FileReader();
      reader.onload = e => {
        this.user.avatar = e.target.result;
      };
      reader.readAsDataURL(file);
    },
    show(popup_name) {
      this.fetchUserbyID();
      this.$modal.show(popup_name);
      setTimeout(() => {
        this.user = {
          ...this.getUserEditor,
          avatar: null
        };
      }, 1000);
    },
    onSaveUserClick() {
      this.putPersonUpdate(this.user);
      setTimeout(() => {
        this.fetchUserByUsername();
      }, 1000);
      setTimeout(() => {
        if (
          this.getUserByUsername != undefined ||
          this.getUserByUsername != null
        ) {
          // this.user_infor.avatar = this.getUserByUsername.avatar;
          this.user_infor.fullname = this.getUserByUsername.fullname;
        } else {
          // this.user_infor.avatar = localStorage.getItem(DATA_NAME_AVATAR);
          this.user_infor.fullname = localStorage.getItem(DATA_NAME_FULLNAME);
        }
        this.$modal.hide("new-user-popup");
      }, 1000);
    },
    onSavePasswordClick(){
      if(this.user_pw.password == null || this.user_pw.password2 == null || this.user_pw.pw == null ){
        this.user_pw.error = '';
        this.user_pw.error_empty = "Password can't empty";
        return;
      }
      if(this.user_pw.password === this.user_pw.password2){
        setTimeout(() => {
          this.putUserPassword(this.user_pw);
          this.$modal.hide("password-user-popup");
          this.user_pw.error_empty = '';
        this.user_pw.error = '';
        }, 1000);
      }
      else{
        this.user_pw.error_empty = '';
        this.user_pw.error = "Password doesn't match";
        return;
      }
      
    }
  },
  mounted: function() {
    this.setWidthMenu(this.$refs.sidebar.getBoundingClientRect().width);
    this.fetchUserByUsername();
    setTimeout(() => {
      if (
        this.getUserByUsername != undefined ||
        this.getUserByUsername != null
      ) {
        this.user_infor.avatar = this.getUserByUsername.avatar;
        this.user_infor.fullname = this.getUserByUsername.fullname;
      } else {
        this.user_infor.avatar = localStorage.getItem(DATA_NAME_AVATAR);
        this.user_infor.fullname = localStorage.getItem(DATA_NAME_FULLNAME);
      }
      this.fetchSessionDate();
    }, 1000);
    setTimeout(() => {
      // load booking for front desk and notify
      this.fetchRooms();
      this.fetchBookings(format(this.getSessionDate, "YYYY-MM-DD"));
      // load booking for front desk and notify
    }, 2000);
  }
};
</script>
