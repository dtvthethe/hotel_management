<template>
  <div id="head-bar">
    <!--header start-->
    <header class="header fixed-top clearfix">
      <!--logo start-->
      <div class="brand">
        <a href="index.html" class="logo">Hoàng Lộc Hotel</a>
        <div class="sidebar-toggle-box">
          <div class="fa fa-bars" @click="switchMenu()"></div>
        </div>
      </div>
      <!--logo end-->
      <div class="nav notify-row" id="top_menu">
        <!--  notification start -->
        <ul class="nav top-menu">
          <!-- settings start -->
          <li class="dropdown">
            <a data-toggle="dropdown" class="dropdown-toggle" href="#">
              <i class="fa fa-tasks"></i>
              <span class="badge bg-success">8</span>
            </a>
            <ul class="dropdown-menu extended tasks-bar">
              <li>
                <p class>You have 8 pending tasks</p>
              </li>
              <li>
                <a href="#">
                  <div class="task-info clearfix">
                    <div class="desc pull-left">
                      <h5>Target Sell</h5>
                      <p>25% , Deadline 12 June’13</p>
                    </div>
                    <span class="notification-pie-chart pull-right" data-percent="45">
                      <span class="percent"></span>
                    </span>
                  </div>
                </a>
              </li>
              <li>
                <a href="#">
                  <div class="task-info clearfix">
                    <div class="desc pull-left">
                      <h5>Product Delivery</h5>
                      <p>45% , Deadline 12 June’13</p>
                    </div>
                    <span class="notification-pie-chart pull-right" data-percent="78">
                      <span class="percent"></span>
                    </span>
                  </div>
                </a>
              </li>
              <li>
                <a href="#">
                  <div class="task-info clearfix">
                    <div class="desc pull-left">
                      <h5>Payment collection</h5>
                      <p>87% , Deadline 12 June’13</p>
                    </div>
                    <span class="notification-pie-chart pull-right" data-percent="60">
                      <span class="percent"></span>
                    </span>
                  </div>
                </a>
              </li>
              <li>
                <a href="#">
                  <div class="task-info clearfix">
                    <div class="desc pull-left">
                      <h5>Target Sell</h5>
                      <p>33% , Deadline 12 June’13</p>
                    </div>
                    <span class="notification-pie-chart pull-right" data-percent="90">
                      <span class="percent"></span>
                    </span>
                  </div>
                </a>
              </li>

              <li class="external">
                <a href="#">See All Tasks</a>
              </li>
            </ul>
          </li>
          <!-- settings end -->
          <!-- inbox dropdown start-->
          <li id="header_inbox_bar" class="dropdown">
            <a data-toggle="dropdown" class="dropdown-toggle" href="#">
              <i class="fa fa-envelope-o"></i>
              <span class="badge bg-important">4</span>
            </a>
            <ul class="dropdown-menu extended inbox">
              <li>
                <p class="red">You have 4 Mails</p>
              </li>
              <li>
                <a href="#">
                  <span class="photo">
                    <img alt="avatar" src="../assets/images/3.png">
                  </span>
                  <span class="subject">
                    <span class="from">Jonathan Smith</span>
                    <span class="time">Just now</span>
                  </span>
                  <span class="message">Hello, this is an example msg.</span>
                </a>
              </li>
              <li>
                <a href="#">
                  <span class="photo">
                    <img alt="avatar" src="../assets/images/1.png">
                  </span>
                  <span class="subject">
                    <span class="from">Jane Doe</span>
                    <span class="time">2 min ago</span>
                  </span>
                  <span class="message">Nice admin template</span>
                </a>
              </li>
              <li>
                <a href="#">
                  <span class="photo">
                    <img alt="avatar" src="../assets/images/3.png">
                  </span>
                  <span class="subject">
                    <span class="from">Tasi sam</span>
                    <span class="time">2 days ago</span>
                  </span>
                  <span class="message">This is an example msg.</span>
                </a>
              </li>
              <li>
                <a href="#">
                  <span class="photo">
                    <img alt="avatar" src="../assets/images/2.png">
                  </span>
                  <span class="subject">
                    <span class="from">Mr. Perfect</span>
                    <span class="time">2 hour ago</span>
                  </span>
                  <span class="message">Hi there, its a test</span>
                </a>
              </li>
              <li>
                <a href="#">See all messages</a>
              </li>
            </ul>
          </li>
          <!-- inbox dropdown end -->
          <!-- notification dropdown start-->
          <li id="header_notification_bar" class="dropdown">
            <a data-toggle="dropdown" class="dropdown-toggle" href="#">
              <i class="fa fa-bell-o"></i>
              <span class="badge bg-warning">3</span>
            </a>
            <ul class="dropdown-menu extended notification">
              <li>
                <p>Notifications</p>
              </li>
              <li>
                <div class="alert alert-info clearfix">
                  <span class="alert-icon">
                    <i class="fa fa-bolt"></i>
                  </span>
                  <div class="noti-info">
                    <a href="#">Server #1 overloaded.</a>
                  </div>
                </div>
              </li>
              <li>
                <div class="alert alert-danger clearfix">
                  <span class="alert-icon">
                    <i class="fa fa-bolt"></i>
                  </span>
                  <div class="noti-info">
                    <a href="#">Server #2 overloaded.</a>
                  </div>
                </div>
              </li>
              <li>
                <div class="alert alert-success clearfix">
                  <span class="alert-icon">
                    <i class="fa fa-bolt"></i>
                  </span>
                  <div class="noti-info">
                    <a href="#">Server #3 overloaded.</a>
                  </div>
                </div>
              </li>
            </ul>
          </li>
          <!-- notification dropdown end -->
        </ul>
        <!--  notification end -->
      </div>
      <div class="top-nav clearfix">
        <!--search & user info start-->
        <ul class="nav pull-right top-menu">
          <li>
            <input type="text" class="form-control search" placeholder=" Search">
          </li>
          <!-- user login dropdown start-->
          <li class="dropdown">
            <a data-toggle="dropdown" class="dropdown-toggle" href="#">
              <img alt src="../assets/images/2.png">
              <span class="username">John Doe</span>
              <b class="caret"></b>
            </a>
            <ul class="dropdown-menu extended logout">
              <li>
                <a href="#">
                  <i class="fa fa-suitcase"></i>Profile
                </a>
              </li>
              <li>
                <a href="#">
                  <i class="fa fa-cog"></i> Settings
                </a>
              </li>
              <li>
                <a href="javascript:void(0);" @click="onLogOutClick">
                  <i class="fa fa-key"></i> Log Out
                </a>
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
                <span>Report x</span>
              </a>
              <ul class="sub">
                <li>
                  <a href="#">Pending Check-in</a>
                </li>
                <li>
                  <a href="#">Pending Check-out</a>
                </li>
                <li>
                  <a href="#">In-House List</a>
                </li>
                <li>
                  <a href="#">Breakfast List</a>
                </li>
                <li>
                  <a href="#">HouseSkeeping</a>
                </li>
                <li>
                  <a href="#">Daily Payment</a>
                </li>
                <li>
                  <a href="#">Extra Charge</a>
                </li>
              </ul>
            </li>
            <li class="sub-menu">
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
            </li>
            <li class="sub-menu">
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
            </li>
            <li class="sub-menu">
              <router-link to="/user">
                <i class="fa fa-user"></i>
                <span>User Management</span>
              </router-link>
            </li>
          </ul>
        </div>
        <!-- sidebar menu end-->
      </div>
    </aside>
    <!--sidebar end-->
  </div>
</template>

<script>
import { mapActions } from "vuex";

export default {
  name: "HeadBar",
  computed: {},
  methods: {
    ...mapActions({
      switchMenu: "switchMenu",
      setWidthMenu: "setWidthMenu",
      removeTokenLocal: "removeTokenLocal"
    }),
    onLogOutClick() {
      this.removeTokenLocal();
    }
  },
  mounted: function() {
    this.setWidthMenu(this.$refs.sidebar.getBoundingClientRect().width);
  }
};
</script>
