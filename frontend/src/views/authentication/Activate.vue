<template>
  <div class="col-md-6 mx-auto">
    <template v-if="activated == false">
      Activating your account...
    </template>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      activated: false
    };
  },
  mounted() {
    axios
      .post("http://localhost:8000/account/activate/", {
        token: this.$route.query.token
      })
      .then(
        setTimeout(() => {
          this.activated = true;
        }, 4000)
      )
      .then(
        setTimeout(() => {
          this.$router.push({ name: "Login" });
        }, 1000)
      );
  }
};
</script>
