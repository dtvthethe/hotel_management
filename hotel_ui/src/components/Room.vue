<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Rooms</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <a class="btn btn-sm btn-default" @click="show('editor-popup')">Add new Item</a>
      <select v-model="room_type_id">
        <option :value="0" >All</option>
        <option :key="item.id" :value="item.id" v-for="item in getRoomTypess">{{item.name}}</option>
      </select>
      <table class="table table-striped">
        <thead>
          <tr>
            <th data-breakpoints="xs">#</th>
            <th>Name</th>
            <th>Room Type</th>
            <th>Status</th>
            <th>Price</th>
            <th>Capacity</th>
            <th>Options</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in roomFilter">
            <td>{{index + 1}}</td>
            <td>{{item.name}}</td>
            <td>{{item.room_type.name}}</td>
            <td>{{item.room_status.name}}</td>
            <td>{{item.price | currency}}</td>
            <td>{{item.capacity}}</td>
            <td>
              <a style="cursor: pointer;" @click="show('editor-popup', item.id)">Edit</a> |
              <a style="cursor: pointer;" @click="showDelete(item.id)">Delete</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Modal -->
    <popup-modal name="editor-popup" :clickToClose="false" :height="350">
      <br>Name:
      <input type="input" v-model="objApi.name">
      <br>Room status:
      <select v-model="objApi.room_status">
        <option :key="item.id" :value="item.id" v-for="item in getRoomStatus">{{item.name}}</option>
      </select>
      <br>Room type:
      <select v-model="objApi.room_type">
        <option :key="item.id" :value="item.id" v-for="item in getRoomTypess">{{item.name}}</option>
      </select>
      <br>Price:
      <input type="input" v-model="objApi.price"> {{objApi.price | currency}}
      <br>Capacity:
      <input type="input" v-model="objApi.capacity">
      <br>

      <input type="button" value="Save" @click="onSaveClick()">
      <input type="button" value="Close" @click="hide('editor-popup')">
    </popup-modal>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Room",
  data() {
    return {
      room_type_id: 0,
      objApi: {
        id: 0,
        room_status: 0,
        room_type: 0,
        name: null,
        price: 0,
        capacity: 0
      },
      room:{
        id: 0,
        room_status: 0,
        room_type: 0,
        name: null,
        price: 0,
        capacity: 0
      }
    };
  },
  computed: {
    ...mapGetters({
      getRoomss:'getRoomss',
      getRoom:'getRoom',
      getRoomTypess:'getRoomTypess',
      getRoomStatus:'getRoomStatus'
    }),
    roomFilter(){
      if(this.room_type_id > 0){
        return this.getRoomss.filter(item => item.room_type.id == this.room_type_id);
      }
      return this.getRoomss;
    }
  },
  methods: {
    ...mapActions({
      fetchRoomss:'fetchRoomss',
      postRoom:'postRoom',
      putRoom:'putRoom',
      deleteRoom:'deleteRoom',
      fetchRoomTypess:'fetchRoomTypess',
      fetchRoomStatus:'fetchRoomStatus'
    }),
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    show(popup_name, id = null) {
      if (id != null) {
        let room = this.getRoom(id);
        this.objApi = {
          ...room,
          room_status: room.room_status.id,
          room_type: room.room_type.id,
        }
      }
      else{
        this.objApi = this.room;
        this.objApi.id = 0;
        this.objApi.name = '';
        this.objApi.price = 0;
        this.objApi.capacity = 0;
      }
      this.$modal.show(popup_name);
    },
    onSaveClick() {
      if (this.objApi.id <= 0) {
        this.postRoom(this.objApi);
      } else {
        this.putRoom(this.objApi);
      }
      setTimeout(() => {
        this.fetchRoomss();
        this.$modal.hide("editor-popup");
      }, 2000);
    },
    showDelete(id) {
      this.$dialog
        .confirm("Do you want to delete this item?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          this.deleteRoom(id);
          setTimeout(() => {
            this.fetchRoomss();
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    }
  },
  mounted: function() {
    this.fetchRoomTypess();
    this.fetchRoomStatus();
    this.fetchRoomss();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
