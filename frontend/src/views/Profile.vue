<template>
  <v-row>
    <v-card float-left class="mx-auto my-12" max-width="374">
      <v-img
        height="350"
        src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
      ></v-img>
      <v-card-title class="m-4">
        {{ whoami.username }}
      </v-card-title>

      <v-divider class="mx-4"></v-divider>
      <v-card-actions>
        <v-btn text @click="formIsVisible = !formIsVisible">
          Update Profile
        </v-btn>
      </v-card-actions>

      <form v-if="formIsVisible" class="p-2">
        <v-text-field
          type="text"
          placeholder="First Name"
          v-model="whoami.first_name"
        ></v-text-field>
        <v-text-field
          :value="whoami.last_name"
          type="text"
          placeholder="Last Name"
        ></v-text-field>
        <v-text-field
          v-model="whoami.email"
          type="text"
          placeholder="Email"
        ></v-text-field>
        <v-text-field
          type="text"
          v-model="whoami.date_of_birth"
          placeholder="Date Of Birth"
        ></v-text-field>
        <v-btn
          dark
          color="grey darken-2"
          block
          x-large
          class="btn-block"
          @click="updateUser"
          >Update</v-btn
        >
      </form>
    </v-card>
    <!-- 
    <v-card float-right class="mx-auto my-12 col-md-8">
      <div v-for="action in actions" :key="action.id" class="col-md-12">EVENT_DESCRIPTION</div>
    </v-card> -->
  </v-row>
</template>

<script>
// import axios from "axios";
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      formIsVisible: false
    };
  },
  mounted() {
    // console.log(this.whoami.first_name)
  },
  computed: {
    ...mapState({
      whoami: state => state.authentication.whoami
    })
  },
  methods: {
    ...mapActions(["whoamiUpdate"]),
    updateUser(event) {
      // let payload = {
      //   'refresh_token': this.whoami.refresh_token,
      //   'access_token': this.whoami.access_token,
      //   'id': this.whoami.id,
      //   'username': this.whoami.username,
      //   'email': this.whoami.email,
      //   'first_name': this.whoami.first_name,
      //   'last_name': this.whoami.last_name,
      //   'date_of_birth': this.whoami.date_of_birth,
      //   'photo': this.whoami.photo,
      // }
      console.log(event.target.value);
      // this.$store.dispatch("update_current_user_action", this.payload);
    }
  }
};
</script>
