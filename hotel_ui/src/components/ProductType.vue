<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Product Types</h3>
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
          <tr :key="item.id" v-for="(item, index) in getProductTypess">
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
  name: "ProductType",
  data() {
    return {
      objApi: {
        id: 0,
        name: null
      },
      producttype: {
        id: 0,
        name: null
      }
    };
  },
  computed: {
    ...mapGetters({
      getProductTypess:'getProductTypess',
      getProductType:'getProductType'
    })
  },
  methods: {
    ...mapActions({
      fetchProductTypess:'fetchProductTypess',
      postProductType:'postProductType',
      putProductType:'putProductType',
      deleteProductType:'deleteProductType'
    }),
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    show(popup_name, id = null) {
      if (id != null) {
        this.objApi = this.getProductType(id);
      }
      else{
        this.objApi = this.producttype;
        this.objApi.id = 0;
        this.objApi.name = '';
      }
      this.$modal.show(popup_name);
    },
    onSaveClick() {
      if (this.objApi.id <= 0) {
        this.postProductType(this.objApi);
      } else {
        this.putProductType(this.objApi);
      }
      setTimeout(() => {
        this.fetchProductTypess();
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
          this.deleteProductType(id);
          setTimeout(() => {
            this.fetchProductTypess();
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    }
  },
  mounted: function() {
    this.fetchProductTypess();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
