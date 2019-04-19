<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>Product</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <a class="btn btn-sm btn-default" @click="show('editor-popup')">Add new Item</a>
      <select v-model="product_type_id">
        <option :value="0" >All</option>
        <option :value="item.id" :key="item.id"  v-for="item in getProductTypess">{{item.name}}</option>
      </select>
      <table class="table table-striped">
        <thead>
          <tr>
            <th data-breakpoints="xs">#</th>
            <th>Name</th>
            <th>Type</th>
            <th>Options</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="item.id" v-for="(item, index) in productFilter">
            <td>{{index + 1}}</td>
            <td>{{item.name}}</td>
            <td>{{item.product_type.name}}</td>
            <td>{{item.price | currency}}</td>
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
      <br>Price:
      <input type="input" v-model="objApi.price">{{objApi.price | currency}}
      <br>Product Type:
      <select v-model="objApi.product_type">
        <option :value="item.id" :key="item.id"  v-for="item in getProductTypess">{{item.name}}</option>
      </select>


      <input type="button" value="Save" @click="onSaveClick()">
      <input type="button" value="Close" @click="hide('editor-popup')">
    </popup-modal>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "Product",
  data() {
    return {
      product_type_id: 0,
      objApi: {
        id: 0,
        name: null,
        price: 0,
        product_type:0
      },
      product:{
        id: 0,
        name: null,
        price: 0,
        product_type:0
      }
    };
  },
  computed: {
    ...mapGetters({
      getProducts:'getProducts',
      getProduct:'getProduct',
      getProductTypess:'getProductTypess',
    }),
    productFilter(){
      if(this.product_type_id > 0){
        return this.getProducts.filter(item => item.product_type.id == this.product_type_id);
      }
      return this.getProducts;
    }
  },
  methods: {
    ...mapActions({
      fetchProductss:'fetchProductss',
      postProduct:'postProduct',
      putProduct:'putProduct',
      deleteProduct:'deleteProduct',
      fetchProductTypess:'fetchProductTypess'
    }),
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    show(popup_name, id = null) {
      if (id != null) {
        let product = this.getProduct(id);
        this.objApi = {
          ...product,
          product_type:product.product_type.id
        }
      }
      else{
        this.objApi = this.product;
        this.objApi.name = '';
        this.objApi.id = 0;
        this.objApi.price = 0;
      }
      this.$modal.show(popup_name);
    },
    onSaveClick() {
      if (this.objApi.id <= 0) {
        this.postProduct(this.objApi);
      } else {
        this.putProduct(this.objApi);
      }
      setTimeout(() => {
        this.fetchProductss();
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
          this.deleteProduct(id);
          setTimeout(() => {
            this.fetchProductss();
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
    this.fetchProductss();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}

</style>
