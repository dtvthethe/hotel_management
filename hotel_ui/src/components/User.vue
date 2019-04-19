<template>
  <div>
    <header class="agileits-box-header clearfix">
      <h3>User</h3>
      <div class="toolbar"></div>
    </header>
    <div class="table-responsive bg-white">
      <a class="btn btn-sm btn-default" @click="show('new-user-popup')">Add new User</a>
      <table class="table table-striped">
        <thead>
          <tr>
            <th data-breakpoints="xs">#</th>
            <th>Username</th>
            <th>Fullname</th>
            <th>Email</th>
            <th>Status</th>
            <th>Options</th>
          </tr>
        </thead>
        <tbody>
          <tr :key="user.id" v-for="(user, index) in getUsers">
            <td>{{index + 1}}</td>
            <td>{{user.username}}</td>
            <td>{{user.first_name + ' ' + user.last_name}}</td>
            <td>{{user.email}}</td>
            <td>{{user.is_active == 1 ? 'Active' : 'Block'}}</td>
            <td>
              <a style="cursor: pointer;" @click="show('new-user-popup', user.id)">Edit</a> |
              <a style="cursor: pointer;" @click="showPw(user.id)">Reset Password</a> |
              <a v-show="user.id != 1" style="cursor: pointer;" @click="showDelete(user.id)">Delete</a>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
    <!-- Modal -->
    <popup-modal name="new-user-popup" :clickToClose="false" :height="350">
      <div v-if="user.id <= 0">
      password:
      <input type="password" v-model="user.password">
      </div>
      super user:
      <input :disabled="user.id == 1" type="checkbox" v-model="user.is_superuser">
      <br>username:
      <input :disabled="user.id > 0" type="input" v-model="user.username">
      <br>first name:
      <input type="input" v-model="user.first_name">
      <br>last name:
      <input type="input" v-model="user.last_name">
      <br>email address:
      <input type="email" v-model="user.email">
      <br>Staff:
      <input type="checkbox" checked disabled>
      <br>Active:
      <input type="checkbox" v-model="user.is_active">
      <br>
      <ul class="lst-permission">
        <li :key="item.id" v-for="item in getUserPermissions">
          <label :for="'perm-'+item.id">
            <input
              type="checkbox"
              :value="item.id"
              :id="'perm-'+item.id"
              v-model="user.user_permissions"
            >
            {{item.codename}} ({{item.name}})
          </label>
        </li>
      </ul>

      <input type="button" value="Save" @click="onSaveUserClick()">
      <input type="button" value="Close" @click="hide('new-user-popup')">
    </popup-modal>

    <popup-modal name="reset-pass-popup" :clickToClose="false" :height="350">
      password:
      <input
        type="password"
        id="txtpw3"
        name="txtpw3"
        v-model="user_pw.pw"
      >

      <input type="button" value="Save" @click="onSavePasswordClick()">
      <input type="button" value="Close" @click="hide('reset-pass-popup')">
    </popup-modal>
    <!-- // Modal -->
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";

export default {
  name: "User",
  data() {
    return {
      user: {
        id: 0,
        is_superuser: 0,
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        is_staff: 1,
        is_active: 0,
        groups: [],
        user_permissions: [],
        password: null
      },
      user_default: {
        id: 0,
        is_superuser: 0,
        username: null,
        first_name: null,
        last_name: null,
        email: null,
        is_staff: 1,
        is_active: 0,
        groups: [],
        user_permissions: [],
        password: null
      },
      user_pw: {
        pw: null,
        id: 0
      }
    };
  },
  computed: {
    ...mapGetters({
      getUsers: "getUsers",
      getUser: "getUser",
      getUserPermissions: "getUserPermissions"
    })
  },
  methods: {
    ...mapActions({
      fetchUsers: "fetchUsers",
      fetchUserPermissions: "fetchUserPermissions",
      postUser: "postUser",
      putUser: "putUser",
      deleteUser: "deleteUser",
      putUserPassword: "putUserPassword"
    }),
    hide(popup_name) {
      this.$modal.hide(popup_name);
    },
    show(popup_name, id = null) {
      if (id != null) {
        this.user = this.getUser(id);
      }
      else{
        this.user = this.user_default;
        this.user.id = 0;
        this.useris_superuser= 0;
        this.userusername= null;
        this.userfirst_name= null;
        this.userlast_name= null;
        this.useremail= null;
        this.useris_staff= 1;
        this.useris_active= 0;
        this.usergroups= [];
        this.useruser_permissions= [];
        this.userpassword= null;
      }
      this.$modal.show(popup_name);
    },
    showPw(id = 0) {
      if (id > 0) {
        this.user_pw.id = id;
        this.$modal.show("reset-pass-popup");
      }
    },
    onSaveUserClick() {
      if (this.user.id <= 0) {
        this.postUser(this.user);
      } else {
        this.putUser(this.user);
      }
      setTimeout(() => {
        this.fetchUsers();
        this.$modal.hide("new-user-popup");
      }, 2000);
    },
    onSavePasswordClick() {
      this.putUserPassword(this.user_pw);
      setTimeout(() => {
        this.$modal.hide("reset-pass-popup");
      }, 2000);
    },
    showDelete(id) {
      this.$dialog
        .confirm("Do you want to delete this user?", {
          loader: true,
          okText: "Yes",
          cancelText: "No"
        })
        .then(dialog => {
          // on OK click
          this.deleteUser(id);
          setTimeout(() => {
            this.fetchUsers();
            dialog.close();
          }, 2000);
        })
        .catch(() => {
          // on cancel click
        });
    }
  },
  mounted: function() {
    this.fetchUsers();
    this.fetchUserPermissions();
  }
};
</script>
<style scoped>
.bg-white {
  background-color: white;
}
.lst-permission {
  height: 100px;
  overflow: auto;
  /* width: 100px; */
  border: 1px solid #000;
  /* list-style-type: none; */
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}
.lst-permission li {
  margin: 0;
  padding: 0;
}
.lst-permission label {
  display: block;
  margin: 0;
  padding: 0;
  width: 100%;
}
.lst-permission label:hover {
  background-color: Highlight;
  color: HighlightText;
}
</style>
