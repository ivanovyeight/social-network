<template>
  <v-app>
    <v-app-bar app color="dark-2" dark>
      <v-row v-if="!whoami.access_token && !whoami.username">
        <v-btn text class="mr-2" to="/register">Register</v-btn>
        <v-spacer></v-spacer>
        <v-btn text class="mr-2" to="/login">Login</v-btn>
      </v-row>
      <v-row v-else>
        <v-btn text class="mr-2" to="/profile">Profile</v-btn>
        <v-btn text class="mr-2" to="/about">About</v-btn>
        <v-spacer></v-spacer>
        <v-btn text class="mr-2" v-on:click="handleLogout">Logout</v-btn>
      </v-row>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapState } from "vuex";
export default {
  name: "App",
  computed: {
    ...mapState({
      whoami: state => state.authentication.whoami
    })
  },
  methods: {
    handleLogout(event) {
      event.preventDefault();
      this.logout();
      if (this.$route.path != "/") {
        this.$router.push("/");
      }
    },
    ...mapActions(["logout"])
  }
};
</script>
