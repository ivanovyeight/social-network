<template>
  <v-container class="col-md-8">
    <ProfileForm></ProfileForm>
    <PaymentsComponent></PaymentsComponent>
  </v-container>
</template>

<script>
import ProfileForm from "../components/ProfileForm";
import PaymentsComponent from "../components/PaymentsComponent";

export default {
  components: { ProfileForm, PaymentsComponent }
};
</script>
