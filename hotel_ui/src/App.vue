<template>
  <div id="app">
    <!-- {{getTokenAuth}} -->
    <template v-if="getTokenAuth != null">
      <HeadBar></HeadBar>
      <!--main content start-->
      <section id="main-content">
        <section class="wrapper">
          <section class="agile-grid">
            <router-view></router-view>
          </section>
        </section>
        <!-- footer -->
        <div class="footer">
          <div class="wthree-copyright">
            <p>© 2019 HOANGLOCHOTEL. All rights reserved</p>
          </div>
        </div>
        <!-- / footer -->
      </section>
      <!--main content end-->
    </template>
    <template v-else>
      <div class="log-w3">
        <div class="w3layouts-main">
          <h2>HOANG LOC Hotel</h2>
          <div>
            <div class="alert alert-danger" v-if="msgLoginError != null">
              <strong>Lỗi!</strong> {{msgLoginError}}
            </div>
            <input
              type="text"
              class="ggg"
              name="Username"
              placeholder="USERNAME"
              v-model="data_login.username"
            >
            <input
              type="password"
              class="ggg"
              name="Password"
              placeholder="PASSWORD"
              v-model="data_login.password"
            >
            <div class="clearfix"></div>
            <input type="submit" value="Sign In" name="login" @click="loginClick()">
          </div>
        </div>
      </div>
    </template>
  </div>
</template>

<script>
import HeadBar from "./components/HeadBar";
import { mapActions, mapGetters } from "vuex";
// import { NAME_TOKEN } from './store/config'

export default {
  name: "app",
  data: function() {
    return {
      data_login: {
        username: null,
        password: null
      },
      msgLoginError: null
    };
  },
  components: {
    HeadBar
  },
  computed: {
    ...mapGetters({ getTokenAuth: "getTokenAuth" })
  },
  methods: {
    ...mapActions({
      postUserlogin: "postUserlogin",
      verifyToken: "verifyToken",
      getTokenfromLocal:"getTokenfromLocal"
    }),
    loginClick() {
      this.postUserlogin(this.data_login);
      if (this.getTokenAuth == null) {
        this.msgLoginError = "Sai tài khoản hoặc mật khẩu.";
      }
    },
  },
  created() {
    this.getTokenfromLocal();
    if(this.getTokenAuth != undefined && this.getTokenAuth != null){
      this.verifyToken({'token': this.getTokenAuth});
    }
  }
};
</script>

<style>
</style>
