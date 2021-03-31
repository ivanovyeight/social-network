<template>
  <v-container>
    <v-card>
      <v-container class="offset-md-4">
        <v-avatar color="grey" size="256" round>
          <v-img
            src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
            alt="..."
          ></v-img>
        </v-avatar>
      </v-container>
      <form>
        <div class="container">
          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                type="text"
                placeholder="First Name"
                v-model="first_name"
                filled
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="last_name"
                type="text"
                placeholder="Last Name"
                filled
              ></v-text-field>
            </v-col>
          </v-row>
          <v-row>
            <v-col cols="12" md="6">
              <v-text-field
                v-model="email"
                type="text"
                placeholder="Email"
                filled
              ></v-text-field>
            </v-col>
            <v-col cols="12" md="6">
              <v-text-field
                type="text"
                v-model="date_of_birth"
                placeholder="Date Of Birth"
                filled
              ></v-text-field>
            </v-col>
          </v-row>
        </div>
      </form>
    </v-card>
  </v-container>
</template>

<script>
import { mapState, mapActions } from "vuex";

export default {
  components: {
    // ValidationProvider,
    // ValidationObserver
  },
  data() {
    return {
      // username: "",
      // password: ""
    };
  },
  methods: {
    ...mapActions(["iamUpdate"])
  },
  computed: {
    ...mapState({
      iam: state => state.auth.iam
    }),
    first_name: {
      get() {
        return this.iam.first_name;
      },
      set(value) {
        this.iamUpdate({ key: "first_name", value });
      }
    },
    last_name: {
      get() {
        return this.iam.last_name;
      },
      set(value) {
        this.iamUpdate({ key: "last_name", value });
      }
    },
    email: {
      get() {
        return this.iam.email;
      },
      set(value) {
        this.iamUpdate({ key: "email", value });
      }
    },
    date_of_birth: {
      get() {
        return this.iam.date_of_birth;
      },
      set(value) {
        this.iamUpdate({ key: "date_of_birth", value });
      }
    }
  }
};
</script>
