<template>
  <div>
    <select v-model="roomSelectId">
      <option :key="room.id" :value="room.id" v-for="room in getRooms">{{room.name}}</option>
    </select>
    <input type="button" @click="savePopup" value="Save" />
    <input type="button"  @click="closePopup" value="Close" />
  </div>
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
