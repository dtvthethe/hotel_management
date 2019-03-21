<template>
  <div @click="disableMenuContext">
    <header class="agileits-box-header clearfix">
      <h3>Visitor Statistics</h3>
      <div class="toolbar"></div>
    </header>
    <div class="front-desk">
      <div class="front-desk-group">
        <div class="front-desk-title row">
          <strong>Apartment</strong>
        </div>
        <div class="front-desk-body row">
          <div class="col-xs-3 col-md-1 room">
            <div
              class="room-containt room-pending-check-out"
              oncontextmenu="return false"
              @mouseup="enableMenuContext"
            >
              <p class="room-number">303</p>
              <i class="fa fa-plane"></i>
              <p class="room-status">Checkout</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div
              class="room-containt room-pending-check-in"
              oncontextmenu="return false"
              @mouseup="enableMenuContext"
            >
              <p class="room-number">303</p>
              <i class="fa fa-level-down"></i>
              <p class="room-status">Check-in</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-block">
              <p class="room-number">303</p>
              <i class="fa fa-lock"></i>
              <p class="room-status">Block</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-occupied">
              <p class="room-number">303</p>
              <i class="fa fa-smile-o"></i>
              <p class="room-status">Occupied</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-odirty">
              <p class="room-number">303</p>
              <i class="fa fa-magnet"></i>
              <p class="room-status">Dirty</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
        </div>
      </div>

      <div class="front-desk-group">
        <div class="front-desk-title row">
          <strong>Villa</strong>
        </div>
        <div class="front-desk-body row">
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-pending-check-out">
              <p class="room-number">303</p>
              <i class="fa fa-plane"></i>
              <p class="room-status">Checkout</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-pending-check-in">
              <p class="room-number">303</p>
              <i class="fa fa-level-down"></i>
              <p class="room-status">Check-in</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-block">
              <p class="room-number">303</p>
              <i class="fa fa-lock"></i>
              <p class="room-status">Block</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-occupied">
              <p class="room-number">303</p>
              <i class="fa fa-smile-o"></i>
              <p class="room-status">Occupied</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-odirty">
              <p class="room-number">303</p>
              <i class="fa fa-magnet"></i>
              <p class="room-status">Dirty</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
        </div>
      </div>

      <div class="front-desk-group">
        <div class="front-desk-title row">
          <strong>Deluxe King(Double)</strong>
        </div>
        <div class="front-desk-body row">
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-pending-check-out">
              <p class="room-number">303</p>
              <i class="fa fa-plane"></i>
              <p class="room-status">Checkout</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-pending-check-in">
              <p class="room-number">303</p>
              <i class="fa fa-level-down"></i>
              <p class="room-status">Check-in</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-block">
              <p class="room-number">303</p>
              <i class="fa fa-lock"></i>
              <p class="room-status">Block</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-occupied">
              <p class="room-number">303</p>
              <i class="fa fa-smile-o"></i>
              <p class="room-status">Occupied</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-odirty">
              <p class="room-number">303</p>
              <i class="fa fa-magnet"></i>
              <p class="room-status">Dirty</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
          <div class="col-xs-3 col-md-1 room">
            <div class="room-containt room-available">
              <p class="room-number">303</p>
              <i class="fa fa-check-circle"></i>
              <p class="room-status">Available</p>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- Menu Context -->
    <div
      class="row context-menu"
      v-show="context_menu_visible"
      :style="{left:contextMenuLeft+'px', top:contextMenuTop+'px'}"
    >
      <ul class="list-group">
        <li
          data-toggle="modal"
          data-target="#myModal"
          class="list-group-item"
          :key="index"
          v-for="(item, index) in context_menu_list"
        >
          <i :class="item.icon"></i>
          {{item.label}}
        </li>
      </ul>
    </div>
    <!-- //Menu Context -->
    <!-- Modal -->
    <div class="modal fade" id="myModal" tabindex="-1" role="dialog" aria-labelledby="myModalLabel">
      <div class="modal-dialog modal-lg" role="document">
        <div class="modal-content">
          <header class="panel-heading">
            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
              <span aria-hidden="true">&times;</span>
            </button>
            <h4 class="modal-title" id="myModalLabel">Modal title</h4>
          </header>
          <div class="panel-body">
            <div class="">
              <!-- Form here! -->
              <FrmBookingDetail></FrmBookingDetail>
              <!-- //Form here! -->
            </div>
          </div>
        </div>
      </div>
    </div>
    <!-- // Modal -->
  </div>
</template>

<script>
import FrmBookingDetail from "./FrmBookingDetail";

export default {
  name: "FrontDesk",
  components: {
    FrmBookingDetail
  },
  data: function() {
    return {
      context_menu_visible: false,
      contextMenuLeft: 0,
      contextMenuTop: 0,
      context_menu_list: [
        {
          label: "Detail",
          icon: "fa fa-pencil"
        },
        {
          label: "Check-in",
          icon: "fa fa-pencil"
        },
        {
          label: "Check-out",
          icon: "fa fa-pencil"
        }
      ]
    };
  },
  methods: {
    enableMenuContext: function(event) {
      if (event.which === 3) {
        this.contextMenuLeft = event.clientX;
        this.contextMenuTop = event.clientY;
        this.context_menu_visible = !this.context_menu_visible;
      }
      if (event.which === 1) {
        this.context_menu_visible = false;
      }
    },
    disableMenuContext: function(event) {
      this.context_menu_visible = false;
    }
  }
};
</script>

<style scoped>
/* front desk */
.front-desk-group .front-desk-title {
  border-bottom: 1px solid red;
  margin: 5px 0px;
}

.front-desk-group .front-desk-body {
  margin-right: 0px;
  margin-left: 0px;
}
.front-desk-group .front-desk-body .room {
  margin: 5px 0px;
  padding: 0px 5px;
  font-size: 13px;
}
.room .room-containt {
  height: 92px;
  width: 100%;
  border-radius: 4px;
  border: 1px solid #8873a2;
  color: #fff;
  text-align: center;
  cursor: pointer;
}
.room .room-containt .room-number {
  border-bottom: 1px solid #fff;
  border-bottom-style: dashed;
  padding: 2px 0px;
  font-weight: bold;
}

.room .room-containt i {
  font-size: x-large;
  margin: 11px 0px;
}
.room .room-containt .room-status {
  font-size: small;
}
.room-pending-check-out {
  background-color: #f73557;
}
.room-pending-check-in {
  background-color: #207aff;
}
.room-block {
  background-color: #fff;
  color: #000 !important;
}
.room .room-block .room-number {
  border-color: #000;
}
.room-occupied {
  background-color: #e9ad07;
}
.room-odirty {
  background-color: #2a2727;
}
.room-available {
  background-color: #3dc32f;
}
/* front desk */
</style>
