<template>
  <form>
    <h3 class="text-center">Change Room</h3>
    <div class="form-group">
      <label for="room_name">Room</label>
      <select v-model="roomSelectId" id="room_name" class="form-control m-bot15">
        <option :key="room.id" :value="room.id" v-for="room in getRooms">{{room.name}}</option>
      </select>
    </div>
    <input type="button" class="btn btn-success" @click="savePopup" value="Save" />
    <input type="button" class="btn btn-default" style="margin-left: 10px" @click="closePopup" value="Close" />
  </form>
</template>

<script>
import DialogMixin from 'vuejs-dialog/dist/vuejs-dialog-mixin.min.js'

export default {
  name: "ChangeRoomPopupConfirm",
  data:function(){
    return {
      rooms:this.$options.propsData.options.message.rooms,
      roomSelectId: -1,
    }
  },
  mixins:[DialogMixin],
  computed:{
    getRooms(){
      return this.rooms.filter(item=> item.room_status.id != 3);
    }
  },
  methods: {
    savePopup:function(){
      this.proceed({id:this.roomSelectId});
    },
    closePopup:function(){
      this.cancel();
    },
  }
};
</script>
