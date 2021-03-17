<template>
  <ValidationObserver ref="form">
    <v-form @submit.prevent="onSubmit">
      <v-container>
        <ValidationProvider
          name="Username"
          rules="required"
          v-slot="{ errors }"
        >
          <v-text-field
            v-model="username"
            label="Username"
            required
          ></v-text-field>
          <span class="red--text">{{ errors[0] }}</span>
        </ValidationProvider>

        <ValidationProvider
          name="Password"
          rules="required"
          v-slot="{ errors }"
        >
          <v-text-field
            v-model="password"
            label="Password"
            type="password"
            required
          ></v-text-field>
          <span class="red--text">{{ errors[0] }}</span>
        </ValidationProvider>
      </v-container>
      <v-btn
        dark
        color="grey darken-2"
        block
        x-large
        class="btn-block"
        type="submit"
      >
        Login
      </v-btn>
    </v-form>
  </ValidationObserver>
</template>

<script>
import { mapActions } from "vuex";
import { extend, ValidationProvider, ValidationObserver } from "vee-validate";
import { required } from "vee-validate/dist/rules";

extend("required", required);

export default {
  components: {
    ValidationProvider,
    ValidationObserver
  },
  data() {
    return {
      username: "",
      password: ""
    };
  },
  methods: {
    onSubmit() {
      this.$refs.form.validate().then(success => {
        if (!success) {
          return;
        }

        this.login({ username: this.username, password: this.password }).then(
          this.$router.push("/")
        );

      });
    },
    ...mapActions(["login"])
  }
};
</script>
