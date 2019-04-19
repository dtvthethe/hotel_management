<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Room Types</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <a class="btn btn-sm btn-default" @click="show('editor-popup')">Add new Item</a>
      <table class="table table-striped">
        <thead>
          <tr>
            <th data-breakpoints="xs">#</th>
            <th>Name</th>
            <th>Options</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in getRoomTypess">
            <td>{{index + 1}}</td>
            <td>{{item.name}}</td>
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

      <input type="button" value="Save" @click="onSaveClick()">
      <input type="button" value="Close" @click="hide('editor-popup')">
    </popup-modal>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "RoomType",
  data() {
    return {
      objApi: {
        id: 0,
        name: null
      },
      roomtype:{
        id: 0,
        name: null
      }
    };
  },
  computed: {
    ...mapGetters({
      getRoomTypess:'getRoomTypess',
      getRoomType:'getRoomType'
    })
  },
  methods: {
    ...mapActions({
      fetchRoomTypess:'fetchRoomTypess',
      postRoomType:'postRoomType',
      putRoomType:'putRoomType',
      deleteRoomType:'deleteRoomType'
    }),
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    show(popup_name, id = null) {
      if (id != null) {
        this.objApi = this.getRoomType(id);
      }
      else{
        this.objApi = this.roomtype;
        this.objApi.id = 0;
        this.objApi.name = '';
      }
      this.$modal.show(popup_name);
    },
    onSaveClick() {
      if (this.objApi.id <= 0) {
        this.postRoomType(this.objApi);
      } else {
        this.putRoomType(this.objApi);
      }
      setTimeout(() => {
        this.fetchRoomTypess();
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
          this.deleteRoomType(id);
          setTimeout(() => {
            this.fetchRoomTypess();
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
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
