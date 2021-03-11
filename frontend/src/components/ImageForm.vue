<template>
  <ValidationObserver ref="observer" v-slot="{  }">
    <form>
              <v-img
      :src="url"
      :lazy-src="url"
      max-width="500"
      max-height="300"
      ref="image"
    >
      <template v-slot:placeholder>
        <v-row
          class="fill-height ma-0"
          align="center"
          justify="center"
        >
          <v-progress-circular
            indeterminate
            color="grey lighten-5"
          ></v-progress-circular>
        </v-row>
      </template>
      </v-img>

      <ValidationProvider v-slot="{ errors }" name="Title" rules="required|max:30">
        <v-text-field
          v-model="title"
          :counter="30"
          :error-messages="errors"
          label="Title"
          required
        ></v-text-field>
      </ValidationProvider>
        <v-text-field
          v-model="description"
          :counter="150"
          :error-messages="errors"
          label="Description"

        
        ></v-text-field>
      <v-btn class="mr-4" @click="submit">submit</v-btn>
    </form>
  </ValidationObserver>
</template>


<script>
  import { required } from 'vee-validate/dist/rules'
  import { extend, ValidationObserver, ValidationProvider, setInteractionMode } from 'vee-validate'
  import {mapGetters, mapActions} from "vuex"

  setInteractionMode('eager')

  extend('required', {
    ...required,
    message: '{_field_} can not be empty',
  })


  export default {
    name: "ImageForm",
    components: {
      ValidationProvider,
      ValidationObserver,
    },
    data: () => ({
      title: '',
      description: "",
      url: '',

    }),

    methods: {
      imageValidation(){
        let img = document.createElement('img')
        img.src = this.imageData.url
        img.onerror = function(){
          return false
        }
      },
      submit () {
        // if (!this.imageValidation() || this.$refs.observer.validate().isFulfilled()){
        //   this.$refs.observer.validate()
        //   return false
        // }
        let obj = {
          title: this.title,
          url: this.url,
          description: this.description,
        }
        this.saveImageToState(obj)
        this.sendImageObject()
      },
      ...mapActions(["sendImageObject", "saveImageToState"])
    },
    computed: {
      ...mapGetters(["imageData"]),
      
    },
    created(){
      this.title = this.$route.query.title
      this.url = this.$route.query.url
      this.description = ""
      
    }
  }
</script>


<style>
#image{
  margin: auto;
}
</style>

