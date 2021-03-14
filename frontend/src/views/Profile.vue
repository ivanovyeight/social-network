<template>
  <v-row>
    <v-card float-left class="mx-auto my-12" max-width="374">
      <v-img
        height="350"
        src="https://upload.wikimedia.org/wikipedia/commons/7/7c/Profile_avatar_placeholder_large.png"
      ></v-img>
      <v-card-title class="m-4">
        {{ whoami.username }}
        <v-spacer></v-spacer>
        <v-icon @click="formIsVisible = !formIsVisible">mdi-content-copy</v-icon>
      </v-card-title>

      <form v-if="formIsVisible" class="p-2">
        <div class="container">
          <v-text-field
            type="text"
            placeholder="First Name"
            v-model="first_name"
          ></v-text-field>
          <v-text-field
            v-model="last_name"
            type="text"
            placeholder="Last Name"
          ></v-text-field>
          <v-text-field
            v-model="email"
            type="text"
            placeholder="Email"
          ></v-text-field>
          <v-text-field
            type="text"
            v-model="date_of_birth"
            placeholder="Date Of Birth"
          ></v-text-field>
        </div>

      </form>
    </v-card>
    <!-- 
    <v-card float-right class="mx-auto my-12 col-md-8">
      <div v-for="action in actions" :key="action.id" class="col-md-12">EVENT_DESCRIPTION</div>
    </v-card> -->
  </v-row>
</template>

<script>
import { mapState, mapActions } from "vuex";
export default {
  data() {
    return {
      formIsVisible: false
    };
  },
  methods: {
    ...mapActions(['whoamiUpdate'])
  },
  computed: {
    ...mapState({
      whoami: state => state.authentication.whoami
    }),
    first_name: {
      get () {
        return this.whoami.first_name
      },
      set (value) {
        this.whoamiUpdate({key:'first_name', value});
      }
    },
    last_name: {
      get () {
        return this.whoami.last_name
      },
      set (value) {
        this.whoamiUpdate({key:'last_name', value});
      }
    },
    email: {
      get () {
        return this.whoami.email
      },
      set (value) {
        this.whoamiUpdate({key:'email', value});
      }
    },
    date_of_birth: {
      get () {
        return this.whoami.date_of_birth
      },
      set (value) {
        this.whoamiUpdate({key:'date_of_birth', value}); 
      }
    }
  },

};
</script>
