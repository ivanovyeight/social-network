<template>
  <v-app>
    <v-app-bar app color="dark-2" dark>
      <template v-if="!accessTokenIsSet && !isLoggedIn">
        <v-btn text class="mr-2" to="/register">Register</v-btn>
        <v-btn text class="mr-2" to="/login">Login</v-btn>
      </template>
      <template v-else>
        <v-btn text class="mr-2" to="/about">About</v-btn>
        <v-btn text class="mr-2" v-on:click="handleLogout">Logout</v-btn>
      </template>
    </v-app-bar>

    <v-main>
      <router-view></router-view>
      <hr>
    </v-main>
  </v-app>
</template>

<script>
import { mapActions, mapState } from 'vuex';
export default {
  name: 'App',
  computed: {
    ...mapState(['isLoggedIn', 'accessTokenIsSet']),
  },
  methods: {
    handleLogout(event) {
      event.preventDefault();
      this.logout();
      if (this.$route.path != '/') {
        this.$router.push("/");
      }
    },
    ...mapActions(['logout']),
  },
};
</script>
